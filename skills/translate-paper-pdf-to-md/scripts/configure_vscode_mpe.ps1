param(
    [string]$SettingsPath = "$env:APPDATA/Code/User/settings.json"
)
$ErrorActionPreference = 'Stop'
$path = [System.IO.Path]::GetFullPath($SettingsPath)
$text = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

if ($text -notmatch '"\*\.md"\s*:\s*"markdown-preview-enhanced"') {
    $pattern = '("workbench\.editorAssociations"\s*:\s*\{)'
    if ($text -notmatch $pattern) { throw 'workbench.editorAssociations object was not found' }
    $text = [regex]::Replace($text, $pattern, '$1' + "`r`n        `"*.md`": `"markdown-preview-enhanced`",", 1)
}

$settings = [ordered]@{
    'markdown-preview-enhanced.previewMode' = 'Previews Only'
    'markdown-preview-enhanced.automaticallyShowPreviewOfMarkdownBeingEdited' = $true
    'markdown-preview-enhanced.disableAutoPreviewForFilePatterns' = @()
    'markdown-preview-enhanced.markdownParser' = 'markdown-it'
    'markdown-preview-enhanced.mathRenderingOption' = 'KaTeX'
    'markdown-preview-enhanced.mathInlineDelimiters' = '__MPE_INLINE_DELIMITERS__'
    'markdown-preview-enhanced.mathBlockDelimiters' = '__MPE_BLOCK_DELIMITERS__'
    'markdown-preview-enhanced.liveUpdate' = $true
    'markdown-preview-enhanced.hideDefaultVSCodeMarkdownPreviewButtons' = $true
}
foreach ($entry in $settings.GetEnumerator()) {
    # Windows PowerShell emits no pipeline output for an empty array, so
    # ConvertTo-Json must receive it as a direct input object.
    if ($entry.Value -is [string] -and $entry.Value -eq '__MPE_INLINE_DELIMITERS__') {
        $json = '[["$","$"]]'
    } elseif ($entry.Value -is [string] -and $entry.Value -eq '__MPE_BLOCK_DELIMITERS__') {
        $json = '[["$$","$$"]]'
    } else {
        $json = ConvertTo-Json -InputObject $entry.Value -Compress
    }
    $existingPattern = '(?m)^(\s*"' + [regex]::Escape($entry.Key) + '"\s*:).*$'
    if ($text -match $existingPattern) {
        $currentJson = $json
        $text = [regex]::Replace($text, $existingPattern, [System.Text.RegularExpressions.MatchEvaluator]{
            param($match)
            $comma = if ($match.Value.TrimEnd().EndsWith(',')) { ',' } else { '' }
            return $match.Groups[1].Value + ' ' + $currentJson + $comma
        })
        continue
    }
    $last = $text.LastIndexOf('}')
    if ($last -lt 0) { throw 'settings.json has no closing object brace' }
    $prefix = $text.Substring(0,$last).TrimEnd()
    if (-not $prefix.EndsWith(',')) { $prefix += ',' }
    $text = $prefix + "`r`n    `"$($entry.Key)`": $json`r`n" + $text.Substring($last)
}

$temp = $path + '.mpe.tmp'
[System.IO.File]::WriteAllText($temp, $text, [System.Text.UTF8Encoding]::new($false))
Move-Item -LiteralPath $temp -Destination $path -Force
Write-Output "configured=$path"
