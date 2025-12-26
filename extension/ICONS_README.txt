# Icon Placeholder

You need to add 3 PNG icon files to the extension folder:

- icon16.png (16x16 pixels)
- icon48.png (48x48 pixels)  
- icon128.png (128x128 pixels)

## Quick Way to Create Icons

### Option 1: Use an online tool
1. Go to https://www.favicon-generator.org/
2. Upload any image (like a magnifying glass 🔍)
3. Generate and download icons
4. Rename them to icon16.png, icon48.png, icon128.png

### Option 2: Create simple colored squares
1. Open Paint or any image editor
2. Create 128x128 image with solid color (blue/purple)
3. Add text "🔍" or "S"
4. Save as PNG
5. Resize to 48x48 and 16x16 for other sizes

### Option 3: Use PowerShell to create basic icons

Run this PowerShell command in the extension folder to create placeholder icons:

```powershell
# This creates simple colored PNG placeholders
Add-Type -AssemblyName System.Drawing
$sizes = @(16, 48, 128)
foreach ($size in $sizes) {
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $graphics = [System.Drawing.Graphics]::FromImage($bmp)
    $graphics.Clear([System.Drawing.Color]::FromArgb(102, 126, 234))
    $font = New-Object System.Drawing.Font("Arial", [int]($size/2), [System.Drawing.FontStyle]::Bold)
    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $graphics.DrawString("S", $font, $brush, [int]($size/4), [int]($size/4))
    $bmp.Save("icon$size.png", [System.Drawing.Imaging.ImageFormat]::Png)
    $graphics.Dispose()
    $bmp.Dispose()
}
Write-Host "Icons created!"
```

## Temporary Fix

If you want to test without icons immediately, you can comment out the icon references in manifest.json temporarily.
