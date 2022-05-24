# JW URL Bible Citation package for Espanso

An Espanso package to generate Bible JW URL.

You can review your notes and read what a Bible verse says with a simple click. You can also create your own playlists of biblical texts in sign language, with a simple text editor.

<video src="https://github.com/vbastianpc/jw-espanso-package/blob/main/assets/demo-jwurl-bible.mp4?raw=true"></video>


## Requirements

- [Espanso](https://espanso.org/docs/next/install/mac/) 2.1.3-alpha or above
- python3
- [Unidecode](https://pypi.org/project/Unidecode/)


## Installation

Install the package with

```
espanso install jwurl-bible --git https://github.com/vbastianpc/jw-espanso-package.git --external
```

### Update package

```
espanso package update jwurl-bible
```


## Customization

Edit `package.yml` file and choose your language and bible version.

```
espanso edit match/packages/jwurl-bible/package.yml
```

You can edit variables `jw_lang_prefer` and `pub` (see `bibles/bibles.json`)

```yaml
global_vars:
  - name: jw_lang_prefer
    type: echo
    params:
      echo: E # You can edit this...
  - name: pub
    type: echo
    params:
      echo: nwtsty # ...and this
```

## Usage

Type a bible quote preceded by an underscore. Espanso will compare it to the regular expression

```
_(?P<bookname>.*?) ?(?P<chapter>\d+):(?P<verses>\d+(?:[ \-,\d]+)*)\s\s
```

You can test this regular expression at this [link](https://regexr.com/6g6ph). Note that it must end with two whitespaces. Here are some examples


| jw_lang_prefer | pub    | Expression       | URL                                                          | Result                                                       |
| -------------- | ------ | ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| E              | nwtsty | _1 john 3:19, 20 | https://www.jw.org/finder?wtlocale=E&prefer=lang&bible=62003019-62003020&pub=nwtsty | [1 John 3:19, 20](https://www.jw.org/finder?wtlocale=E&prefer=lang&bible=62003019-62003020&pub=nwtsty) |
| E              | nwt    | _1jo 3:19, 20    | https://www.jw.org/finder?wtlocale=E&prefer=lang&bible=62003019-62003020&pub=nwt | [1 John 3:19, 20](https://www.jw.org/finder?wtlocale=E&prefer=lang&bible=62003019-62003020&pub=nwt) |
| S              | nwtsty | _1ju 3:19, 20    | https://www.jw.org/finder?wtlocale=S&prefer=lang&bible=62003019-62003020&pub=nwtsty | [1 Juan 3:19, 20](https://www.jw.org/finder?wtlocale=S&prefer=lang&bible=62003019-62003020&pub=nwtsty) |
| S              | nwtsty | _1jo 3:19, 20    | https://www.jw.org/finder?wtlocale=S&prefer=lang&bible=62003019-62003020&pub=nwtsty | [1 John 3:19, 20](https://www.jw.org/finder?wtlocale=S&prefer=lang&bible=62003019-62003020&pub=nwtsty) |
| VT             | nwt    | _1 gia 3:19, 20  | https://www.jw.org/finder?wtlocale=VT&prefer=lang&bible=62003019-62003020&pub=nwt | [1 Giăng 3:19, 20](https://www.jw.org/finder?wtlocale=VT&prefer=lang&bible=62003019-62003020&pub=nwt) |
| SLV            | nwt    | _1 gia 3:19, 20  | https://www.jw.org/finder?wtlocale=VT&prefer=lang&bible=62003019-62003020&pub=nwt | [1 Giăng 3:19, 20](https://www.jw.org/finder?wtlocale=VT&prefer=lang&bible=62003019-62003020&pub=nwt) |

