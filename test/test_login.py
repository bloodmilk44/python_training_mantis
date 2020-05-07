def test_login(app):
    app.session.login("administrator", "331331eVo5")
    assert app.session.is_logged_in_as("administrator")