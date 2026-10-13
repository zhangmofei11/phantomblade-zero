import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/951bbad4148c6252b596f47ad41e565d"></script>
<script data-cfasync="false" src="https://bauval.org/14/64fdc47668a982b45956f5aef7c962f6"></script>
<script>
  atOptions = {
    'key' : '18aff5f9c73ad50a3c9851721b1bbb64',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/18aff5f9c73ad50a3c9851721b1bbb64"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-951bbad4148c6252b596f47ad41e565d"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'combat.html', 'weapons.html', 'beginner.html', 'endings.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '18aff5f9c73ad50a3c9851721b1bbb64' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-951bbad4148c6252b596f47ad41e565d' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
