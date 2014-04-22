"""Override views to integrate them into Mezzanine's Pages Middleware.

To allow processing through Mezzanine's Page Middleware, views must return a
request that is rendered by mezzanine.utils.views.render.

To upgrade the version of dpaste supported, simply replace the views with their
new versions, ensuring they use Mezzanine's render function instead of Django's
render or render_to_response functions.

"""
from django.shortcuts import (render_to_response, get_object_or_404)
from django.template.context import RequestContext
from django.http import Http404, HttpResponseRedirect
from mezzanine.utils.views import render

from dpaste.forms import SnippetForm
from dpaste.models import Snippet, ONETIME_LIMIT
from dpaste.highlight import LEXER_WORDWRAP, LEXER_LIST


def snippet_new(request, template_name='dpaste/snippet_new.html'):
    """
    Create a new snippet.
    """
    if request.method == "POST":
        snippet_form = SnippetForm(data=request.POST, request=request)
        if snippet_form.is_valid():
            new_snippet = snippet_form.save()
            url = new_snippet.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        snippet_form = SnippetForm(request=request)

    template_context = {
        'snippet_form': snippet_form,
        'lexer_list': LEXER_LIST,
        'is_new': True,
    }

    return render(
        request,
        template_name,
        template_context
    )


def snippet_details(request, snippet_id, template_name='dpaste/snippet_details.html', is_raw=False):
    """
    Details list view of a snippet. Handles the actual view, reply and
    tree/diff view.
    """
    snippet = get_object_or_404(Snippet, secret_id=snippet_id)

    # One time snippet get deleted if the view count matches our limit
    if snippet.expire_type == Snippet.EXPIRE_ONETIME \
    and snippet.view_count >= ONETIME_LIMIT:
        snippet.delete()
        raise Http404()

    # Increase the view count of the snippet
    snippet.view_count += 1
    snippet.save()

    tree = snippet.get_root()
    tree = tree.get_descendants(include_self=True)

    new_snippet_initial = {
        'content': snippet.content,
        'lexer': snippet.lexer,
    }

    if request.method == "POST":
        snippet_form = SnippetForm(
            data=request.POST,
            request=request,
            initial=new_snippet_initial)
        if snippet_form.is_valid():
            new_snippet = snippet_form.save(parent=snippet)
            url = new_snippet.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        snippet_form = SnippetForm(
            initial=new_snippet_initial,
            request=request)

    template_context = {
        'snippet_form': snippet_form,
        'snippet': snippet,
        'lexers': LEXER_LIST,
        'lines': range(snippet.get_linecount()),
        'tree': tree,
        'wordwrap': snippet.lexer in LEXER_WORDWRAP and 'True' or 'False',
    }

    response = render(
        request,
        template_name,
        template_context,
    )

    if is_raw:
        response['Content-Type'] = 'text/plain;charset=UTF-8'
        response['X-Content-Type-Options'] = 'nosniff'
        return response
    else:
        return response
