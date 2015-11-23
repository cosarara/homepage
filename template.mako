<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
        <link href="style.css" rel="stylesheet" title="things">
    </head>
    <body>
        <div class="container">
% for name, url, mime, favicon_data in bmarks:
            <a href="${url}" class="item">
              <img src="data:${mime};base64,${favicon_data}">
              ${name}
            </a>
% endfor
        <div>
    </body>
</html>
