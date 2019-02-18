import markdown
markdown_src = """
```HTML
<!DOCTYPE html>
<html>
<head>
    <link class="remoteCss" rel="stylesheet" type="text/css" tempHref="/css/global.css">
</head>
<body>
    <div id="main"></div>
</body>
</html>
```
"""
print(markdown.markdown(markdown_src, extensions=["codehilite"]))