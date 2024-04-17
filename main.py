import os
import sys
import subprocess
import shutil


def configure_project_path(project_path):
    try:
        if os.path.exists(project_path):
            mapi_file = os.path.expanduser('~/.mapi')
            if not os.path.exists(mapi_file):
                with open(mapi_file, 'w') as f:
                    f.write(project_path)
            else:
                with open(mapi_file, 'w') as f:
                    f.write(project_path)
            print("Project path updated successfully.")
        else:
            raise FileNotFoundError("The given path does not exist.")
    except Exception as e:
        print("Error configuring project path:", str(e))


def get_project_path():
    try:
        mapi_file = os.path.expanduser('~/.mapi')
        if not os.path.exists(mapi_file):
            raise FileNotFoundError("The ~/.mapi file does not exist.")
        with open(mapi_file, 'r') as f:
            project_path = f.read()
            if os.path.exists(project_path):
                return project_path
            else:
                raise FileNotFoundError(
                    "The configured project path does not exist.")
    except FileNotFoundError:
        print("Project path not configured. Please run './main.py configure '")
        sys.exit(1)


def init_project(project_name):
    try:
        project_path = get_project_path()
        if os.path.exists(os.path.join(project_path, project_name)):
            raise FileExistsError(f'Project {project_name} already exists')
        os.mkdir(os.path.join(project_path, project_name))

        # Initialize a new Nodejs project with npm
        subprocess.run(['npm', 'init', '-y'],
                       cwd=os.path.join(project_path, project_name))

        # Install jest
        subprocess.run(['npm', 'install', 'jest'],
                       cwd=os.path.join(project_path, project_name))

        # Create directories
        os.mkdir(os.path.join(project_path, project_name, '__test__'))
        os.mkdir(os.path.join(project_path, project_name, 'config'))
        os.mkdir(os.path.join(project_path, project_name, 'features'))
        os.mkdir(os.path.join(project_path, project_name, 'helpers'))
        os.mkdir(os.path.join(project_path, project_name, 'middleware'))

        # Create files
        with open(os.path.join(project_path, project_name, '.babelrc'), 'w') as f:
            f.write('{}')
        with open(os.path.join(project_path, project_name, 'eslintrc.js'), 'w') as f:
            f.write('module.exports = {}')
        with open(os.path.join(project_path, project_name, '.env'), 'w') as f:
            f.write('')
        with open(os.path.join(project_path, project_name, 'index.js'), 'w') as f:
            f.write('console.log("Hello World");')
        with open(os.path.join(project_path, project_name, 'jest.config.js'), 'w') as f:
            f.write('module.exports = {}')
        with open(os.path.join(project_path, project_name, 'jest.setup.js'), 'w') as f:
            f.write('')

        print(f'Project {project_name} initialized successfully')
    except FileExistsError as e:
        print(str(e))


def create_feature(feature_name):
    try:
        project_path = get_project_path()
        if os.path.exists(os.path.join(project_path, 'features', feature_name)):
            raise FileExistsError(f'Feature {feature_name} already exists')
        os.mkdir(os.path.join(project_path, 'features', feature_name))

        # Create directories
        os.mkdir(os.path.join(project_path, 'features',
                 feature_name, 'controllers'))
        os.mkdir(os.path.join(project_path, 'features', feature_name, 'db'))
        os.mkdir(os.path.join(project_path, 'features', feature_name, 'useCases'))
        os.mkdir(os.path.join(project_path, 'features',
                 feature_name, 'dataAccess'))
        os.mkdir(os.path.join(project_path, 'features', feature_name, 'router'))

        # Create files
        with open(os.path.join(project_path, 'features', feature_name, 'index.js'), 'w') as f:
            f.write(f'export default {{}};')
        with open(os.path.join(project_path, 'features', feature_name, 'db', 'schema.js'), 'w') as f:
            f.write('export default {{}};')

        for dir in ['controllers', 'db', 'useCases', 'dataAccess', 'router']:
            with open(os.path.join(project_path, 'features', feature_name, dir, 'index.js'), 'w') as f:
                f.write(f'export default {{}};')

        print(f'Feature {feature_name} created successfully')
    except FileExistsError as e:
        print(str(e))


def create_helper(helper_name):
    try:
        project_path = get_project_path()
        if os.path.exists(os.path.join(project_path, 'helpers', helper_name)):
            raise FileExistsError(f'Helper {helper_name} already exists')
        os.mkdir(os.path.join(project_path, 'helpers', helper_name))

        # Create index.js file
        with open(os.path.join(project_path, 'helpers', helper_name, 'index.js'), 'w') as f:
            f.write(f'export default {{}};')

        # Add entry to helpers/index.js
        with open(os.path.join(project_path, 'helpers', 'index.js'), 'a') as f:
            f.write(f'import {{helper_name}} from "./{helper_name}";\n')
            f.write(f'export default {{elper_name}};\n')

        print(f'Helper {helper_name} created successfully')
    except FileExistsError as e:
        print(str(e))


def delete_project():
    try:
        project_path = get_project_path()
        if input('Are you sure you want to delete the project? (yes/no) ') == 'yes':
            shutil.rmtree(project_path)
            print('Project deleted successfully')
        else:
            print('Project deletion cancelled')
    except Exception as e:
        print("Error deleting project:", str(e))


def delete_feature(feature_name):
    try:
        project_path = get_project_path()
        if input(f'Are you sure you want to delete the feature {feature_name}? (yes/no) ') == 'yes':
            if os.path.exists(os.path.join(project_path, 'features', feature_name)):
                shutil.rmtree(os.path.join(
                    project_path, 'features', feature_name))
                print(f'Feature {feature_name} deleted successfully')
            else:
                print(f'Feature {feature_name} does not exist')
        else:
            print(f'Feature {feature_name} deletion cancelled')
    except Exception as e:
        print("Error deleting feature:", str(e))


def delete_helper(helper_name):
    try:
        project_path = get_project_path()
        if input(f'Are you sure you want to delete the helper {helper_name}? (yes/no) ') == 'yes':
            if os.path.exists(os.path.join(project_path, 'helpers', helper_name)):
                shutil.rmtree(os.path.join(
                    project_path, 'helpers', helper_name))
                print(f'Helper {helper_name} deleted successfully')
            else:
                print(f'Helper {helper_name} does not exist')
        else:
            print(f'Helper {helper_name} deletion cancelled')
    except Exception as e:
        print("Error deleting helper:", str(e))


def create_test(scenario_name):
    try:
        project_path = get_project_path()
        if os.path.exists(os.path.join(project_path, '__test__', scenario_name)):
            raise FileExistsError(
                f'Test scenario {scenario_name} already exists')
        os.mkdir(os.path.join(project_path, '__test__', scenario_name))

        # Create scenarioName.spec.js file
        with open(os.path.join(project_path, '__test__', scenario_name, f'{scenario_name}.spec.js'), 'w') as f:
            f.write(
                f'describe("{scenario_name}", () => {{\n  it("should pass", () => {{\n    expect(true).toBe(true);\n  }});\n}});\n')

        print(f'Test scenario {scenario_name} created successfully')
    except FileExistsError as e:
        print(str(e))


def main():
    if len(sys.argv) < 2:
        print('Please provide a command')
        return

    command = sys.argv[1]

    if command == 'configure':
        if len(sys.argv) < 3:
            print('Please provide a project path')
            return
        project_path = sys.argv[2]
        configure_project_path(project_path)
    elif command == 'init':
        if len(sys.argv) < 3:
            print('Please provide a project name')
            return
        project_name = sys.argv[2]
        init_project(project_name)
    elif command == 'create':
        if len(sys.argv) < 4:
            print('Please provide a feature or helper name')
            return
        type_ = sys.argv[2]
        name = sys.argv[3]
        if type_ == 'feature':
            create_feature(name)
        elif type_ == 'helper':
            create_helper(name)
        elif type_ == 'test':
            create_test(name)
        else:
            print('Unknown type')
    elif command == 'delete':
        if len(sys.argv) < 3:
            print('Please provide a project, feature or helper name')
            return
        type_ = sys.argv[2]
        if type_ == 'project':
            delete_project()
        elif type_ == 'feature':
            if len(sys.argv) < 4:
                print('Please provide a feature name')
                return
            feature_name = sys.argv[3]
            delete_feature(feature_name)
        elif type_ == 'helper':
            if len(sys.argv) < 4:
                print('Please provide a helper name')
                return
            helper_name = sys.argv[3]
            delete_helper(helper_name)
        else:
            print('Unknown type')
    else:
        print('Unknown command')


if __name__ == '__main__':
    main()
