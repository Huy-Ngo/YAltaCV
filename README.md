# YAltaCV - AltaCV, but with your data in a single YAML file (WIP)

It is time-consuming to goes through the LaTeX file every time you want to update your CV.
Therefore, I have an idea to use some python scripts and GitHub Actions to automatically generate LaTeX fragments to be imported
at those sections. The data that is used for input is in form of a simple YAML file.

To read the original README, see [https://github.com/liantze/AltaCV](liantze/AltaCV)

## Requirements and Compilation

* pdflatex + biber + pdflatex
* AltaCV uses [`fontawesome5`](http://www.ctan.org/pkg/fontawesome5) and [`academicons`](http://www.ctan.org/pkg/academicons); they're included in both TeX Live 2016 and MikTeX 2.9.
* Loading `academicons` is optional: enable it by adding the `academicons` option to `\documentclass`.
* Use the `normalphoto` option to get normal (i.e. non-circular) photos.
* As of v1.2 you can add multiple photos on the left or right: `\photoL{2cm}{logo1}` and `\photoR{2.5cm}{logo2,photo}`. (`\photo` will work like `\photoR`.) Separate your image filenames with commas _without_ spaces.
* Use the `ragged2d` option to activate hyphenations while keeping text left-justified; line endings will thus be less jagged and more aesthetically pleasing.
* As of v1.3 the `withhyper` document class option will make the "personal info" fields into clickable hyperlinks (where it makes sense). See below for more details.
* Can now be compiled with pdflatex, XeLaTeX and LuaLaTeX!
* However if you're using `academicons`, you _must_ use either XeLaTeX or LuaLaTeX. If the doc then compiles but the icons don't show up in the output PDF, try compiling with LuaLaTeX instead.
* The samples here use the [Lato](http://www.latofonts.com/lato-free-fonts/) and [Roboto Slab fonts](https://github.com/googlefonts/robotoslab). Feel free to use a different typeface package instead—often a different typeface will change the entire CV's feel.

## Section types

The `data.yml` file looks like:
```yaml
...
column-1:
    - section-1:
        - item-1: description
        - item-2:
            - prop-1: property
            - prop-2: another property
            - description: Description
column-2:
    - section-2:
        - item-1: description
        - item-2: description
```

Following are 4 types of sections, with their properties:

- `event`:
    - `title`: The name or title of the event
    - `org`: The organization related to this event
    - `time`: The time from start to finish
    - `location`: The location where the even occured
    - `description`: a short abstract if is a string, a bulleted list if is a list
    - Used for life/career events like education/jobs
- `quote`:
    - `quote`: the quote
- `badge`:
    - List of items that are showed as badges
    - `dividertag` is to insert divider between groups of badges
- `scale`:
    - List of items that are showed on scale 0-5
- `referee`:
    - List of referees
    - `name`: name of the referee
    - `institute`: name of the institute
    - `email`: referee's email address
    - `addresses`: list of email addresses

## Plan

Here is what I'm planning to do on this fork:

### Structures

We have these branches:

```
* master - this branch, containing template and data files
pdf - where the pdf files are generated
working - optional branch for pushing works in progress before pulling to master
```

```
├── altacv.cls -- the core functions for the template
├── fragments -- generated tex fragments; in master this would be sample files
│   ├── personal-info.tex
│   ├── skills.tex
│   └── other-info.tex
├── data.yml -- data here
├── generate_tex.py -- this generates tex from yaml
├── Globe_High.png -- this is a picture from the original repo, replace this with your photo for CV
├── LICENSE.md
├── nicethings_icons_readme.txt
├── README.md
├── requirements.txt
├── sample.bib -- for books and publication
└── sample.tex -- the template
```

### Approach

- You push/PR to master
- GA runs the `generate_tex.py` to generate LaTeX fragments into `fragments/`
- These fragments are imported in sample.tex (or any file that is supposed to be your main file), using package `import`
- [https://github.com/xu-cheng/latex-action](xu-cheng/latex-action) runs to compile the TeX file and push to `pdf` branch
