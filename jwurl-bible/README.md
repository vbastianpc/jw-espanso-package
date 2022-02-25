# JW URL Bible Citation package for Espanso

An Espanso package to generate Bible JW URL.

You can review your notes and read what a Bible verse says with a simple click. You can also create your own playlists of biblical texts in sign language, with a simple text editor.

## Installation

Install the package with

`espanso install jwurl-bible --git https://github.com/vbastianpc/jw-espanso-package.git --external`

### Requirements

python3
[Unidecode](https://pypi.org/project/Unidecode/)

## Customization

You can choose your preferred language. 

```espanso edit match/packages/jwurl-bible/package.yml```

Modify the fifth line for an available language (see folder `booknames`)

```yaml
global_vars:
  - name: jw_lang_prefer
    type: echo
    params:
      echo: E
```

How does this affect behavior?

For example, suppose my preferred language is English and then I type: `_Da-ni-en 1:1` . That book was not found in English. So it searches each of the available languages until it matches it in Vietnamese.

## Usage

Type a bible quote preceded by an underscore. Espanso will compare it to the regular expression

```
_(?P<bookname>.*?) ?(?P<chapter>\d+):(?P<verses>\d+(?:[\-,\d]+)*)\s
```

You can test this regular expression at this [link](https://regexr.com/6g6ph)

Here are some examples

| Expression         | Result                                                       |
| ------------------ | ------------------------------------------------------------ |
| _1 Samuel 1:1      | [1 Samuel 1:1](https://www.jw.org/finder?wtlocale=E&bible=09001001) |
| _1sam 1:1          | [1 Samuel 1:1](https://www.jw.org/finder?wtlocale=E&bible=09001001) |
| _1tim3:1-5         | [1 Timothy 3:1-5](https://www.jw.org/finder?wtlocale=E&bible=54003001-54003005) |
| _rev21:3,4         | [Revelation 21:3,4](https://www.jw.org/finder?wtlocale=E&bible=66021003-66021004) |
| _psalms 37:3,4-8   | [Psalms 37:3,4-8](https://www.jw.org/finder?wtlocale=E&bible=19037003-19037008) |
| _Ê-xơ-tê 1:1       | [Ê-xơ-ra 1:1](https://www.jw.org/finder?wtlocale=VT&bible=15001001) |
| _e-xo-te 1:1       | [Ê-xơ-ra 1:1](https://www.jw.org/finder?wtlocale=VT&bible=15001001) |
| _Khai huyen 21:3,4 | [Khải huyền 21:3,4](https://www.jw.org/finder?wtlocale=VT&bible=66021003-66021004) |

