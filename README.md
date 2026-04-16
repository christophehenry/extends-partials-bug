This bug demonstrate how `{% partialdef %}`/`{% partial %}` interact incorrectly with `{% extends %}`/`{% block %}`.

[base.html](extends_partials_bug/templates/base.html) defined a partial named `buttons_inline` and reuse it 
at the bottom of the page. Inside that partial, it also defines a `action_btns_inline` block so that 
template extending `base.html` can redefine the content of the `buttons_inline` partial.

[extended.html](extends_partials_bug/templates/extended.html) tries to redefine the contents of `buttons_inline` 
partial by overriding the `action_btns_inline`. As you can see on that page, overriding the `action_btns_inline` block 
changes the first use of `buttons_inline` partial, but not the second.

The bug is worse when using `{% partialdef %}` without inline as `{% block %}` has no effect whatsoever in the 
extending template. 
