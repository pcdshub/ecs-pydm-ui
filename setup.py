from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().split()

git_requirements = [r for r in requirements if r.startswith('git+')]
requirements = [r for r in requirements if not r.startswith('git+')]
if len(git_requirements) > 0:
    print("User must install the following packages manually:\n"
          "\n".join(f' {r}' for r in git_requirements))

setup(name='lcls_screens',
      author='ECS',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      description='Custom set of pydm screens for LCLS hutches',
      )
