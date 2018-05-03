from model.project import Project


def test_add_project(app):
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    app.project.go_to_projects_page()
    project = Project(name='project_04')
    old_project_list = app.soap.get_projects_list(username, password)
    app.project.create_project(project)
    new_project_list = app.soap.get_projects_list(username, password)
    old_project_list.append(project)
    assert sorted(old_project_list, key=app.project.id_or_max) == sorted(new_project_list, key=app.project.id_or_max)
