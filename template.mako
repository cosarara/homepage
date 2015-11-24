<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Home</title>
        <link href="style.css" rel="stylesheet" title="things">
    </head>
    <body>
      <div class="outer">
        <h1>Home</h1>
        <div class="vline"></div>
        <div class="container">
            % for name, url, mime, favicon_data in bmarks[0][1]:
                <a href="${url}" class="item">
                    <img src="data:${mime};base64,${favicon_data}">
                    ${name}
                </a>
            % endfor
            % for dir_name, marks in bmarks[1:]:
                <div class="collapse" tabindex="1">
                    <div class="name">${dir_name}</div>
                    % for name, url, mime, favicon_data in marks:
                        <a href="${url}" class="item">
                            <img src="data:${mime};base64,${favicon_data}">
                            ${name}
                        </a>
                    % endfor
                </div>
            % endfor
        <div>
      </div>
    </body>
</html>
