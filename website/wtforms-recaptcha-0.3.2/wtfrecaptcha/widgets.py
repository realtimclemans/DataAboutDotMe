from wtforms.widgets import HTMLString

# Template for the widget
RECAPTCHA_HTML = HTMLString(u"""<script type="text/javascript">
      var onloadCallback = function() {
        grecaptcha.render('html_element', {
          'sitekey' : '%(public_key)s'
        });
      };
    </script>
    <script src="https://www.google.com/recaptcha/api.js?onload=onloadCallback&render=explicit"
        async defer>
</script>
      <div id="html_element"></div>""")

class Recaptcha(object):
    """Recaptcha widget that displays HTML depending on security status"""

    def __call__(self, field, **kwargs):
        html = RECAPTCHA_HTML % {
                'protocol': field.secure and 'https' or 'http',
                'public_key': field.public_key
        }
        return html
