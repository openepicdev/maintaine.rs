# maintaine.rs

The **maintaine.rs** book is a curated collection of stories from top **Open Source maintainers**, gathered during [GitHub's Maintainer Month](https://maintainermonth.github.com/) in May 2025.

Each story is written in Markdown and compiled into a beautifully formatted PDF using `pandoc`.

---

## Installing on Debian/Ubuntu

```bash
sudo apt update
sudo apt install pandoc
sudo apt install texlive texlive-latex-extra
```

Follow the instructions from [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) to install the template.

## Generating the PDF

```bash
pandoc ./source/*.md --pdf-engine=pdflatex --from markdown+raw_tex --template eisvogel --metadata-file=./metadata.yaml --listings -o maintainers.pdf
```

## License

All stories are licensed under Creative Commons Attribution-ShareAlike (CC BY-SA). Attribution belongs to each individual author.
