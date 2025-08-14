# Django Home Server

simple web server based on django for home applications, structured storage of files and data and smart home.

## Requirements

- Python 3.13 or higher
- pip (Python package manager)
- The following Python packages:
  - django >= 5.2
  - python-dotenv >= 1.1.0
  - pillow >= 11.1.0

To install the required packages, run:

```bash
pip install -r requirements.txt
```

> [!IMPORTANT]
> This project requires files from the following repository:
> [TiSei/base-web-page](https://github.com/TiSei/base-web-page.git).
> Please download or clone the repository and copy the files located in "/js" and "/css" to a directory of this project, which is part of the static folder. In future development these files come from an external web server

> [!NOTE]
> This project is under development

## Modules

### 3D Libary

storage files for 3d printing, like .stl, .3mf and construction files from FreeCad order by projects. Tags, images and a small notebook are/will be integrated for searching and documentation.

## TODO

- [ ] add noteboook to 3d libary
- [ ] use modified time to sort elements
- [ ] add module "CookBook"
