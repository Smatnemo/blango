from django.template import Library
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = Library()

@register.filter
def author_details(author, current_user):
  if isinstance(author, User):
    if author == current_user:
      print("Am I here?")
      return format_html("<strong>me</strong>")
    print("Did I skip here?")
    if author.first_name and author.last_name:
      name = f"{author.first_name} {author.last_name}"
    else:
      name = f"{author.username}"
    
    if author.email:
      prefix = format_html('<a href="mailto:{}">', author.email)
      suffix = format_html("</a>")
    else:
      prefix = ""
      suffix = ""
    return format_html("{}{}{}", prefix, name, suffix)
  else:
    return ""

# Other answer
def author_details(author):
  if not isinstance(author, User):
    return ""
  
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"
  return name