from selene import browser, have, be


def test_complete_todo(browser_managment):

    browser.open('todomvc/dist/')

    browser.element(".new-todo").type('a').press_enter()
    browser.element(".new-todo").type('b').press_enter()
    browser.element(".new-todo").type('c').press_enter()

    browser.element(".new-todo").should(be.blank)
    browser.all(".todo-list>li").should(have.size(3))

    browser.all(".todo-list>li").first.should(have.text('a'))
    browser.all(".todo-list>li").second.should(have.text('b'))
    browser.all(".todo-list>li")[2].should(have.text('c'))

    browser.all('.todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    browser.all('.todo-list>li').second.element('.toggle').click()

    browser.all('.todo-list>li').by(have.css_class('completed')).should(have.exact_texts('b'))
    browser.all('.todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))
