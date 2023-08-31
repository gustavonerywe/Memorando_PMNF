from django import template
from memoAdmin.settings import BASE_DIR

register = template.Library()

def caminhoFile(file):
    return str(BASE_DIR) + "/" + str(file)

register.filter('caminhoFile', caminhoFile)