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
                <div class="clickable">
                    <label class="name" for="${dir_name}">${dir_name}</label>
                    <input type="checkbox" class="collapse-input" id="${dir_name}" />
                    <div class="collapse">
                        % for name, url, mime, favicon_data in marks:
                            <a href="${url}" class="item">
                                % if favicon_data:
                                    <img src="data:${mime};base64,${favicon_data}">
                                % else:
                                    <div class="no-image"></div>
                                % endif
                                ${name}
                            </a>
                        % endfor
                    </div>
                </div>
            % endfor
        </div>
      </div>
    </body>
</html>
