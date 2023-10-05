# japanese-custom-emoji-naming-convention
japanese-custom-emoji-naming-convention is a bash command + python script that converts Japanese echo text into a string of ASCII-compatible lowercase latin. The naming convention is based on the [Nihonsiki](https://en.wikipedia.org/wiki/Nihon-shiki_romanization) Romanization System for strict transliteration of Japanese. (See ISO 3602 Strict)

## Prerequisities

### JUMAN++

You will need to be able to run `jumanpp` command. Try running `jumanpp -v` in your terminal. Mine looks like this:

```
kawanerio@MoebuntuStudio11:~/jumanpp-1.01$ jumanpp -v
JUMAN++ 1.01 
```

If not installed, please go to [JUMAN](https://nlp.ist.i.kyoto-u.ac.jp/?JUMAN%2B%2B) and install the latest version there. The installation steps may looks something like this: 

```
wget http://lotus.kuee.kyoto-u.ac.jp/nl-resource/jumanpp/jumanpp-1.01.tar.xz
tar xJvf jumanpp-1.01.tar.xz
cd jumanpp-1.01
./configure
make
sudo make install
```


### Python3

You will also need to be able to run `python3`. Try running `python3 --version` on your terminal. Mine looks like this:

```
kawanerio@MoebuntuStudio11:~/jumanpp-1.01$ python3 --version
Python 3.10.12
```

If not installed, try searching "How to install Python3" on the internet. 


### sed

Finally, you should have `sed` installed. Try typing `sed --version` on your terminal. Mine looks like this:

```
kawanerio@MoebuntuStudio11:~/jumanpp-1.01$ sed --version
sed (GNU sed) 4.8
パッケージ作成者: Debian
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

作者 Jay Fenlason、 Tom Lord、 Ken Pizzini、
Paolo Bonzini、 Jim Meyering、および Assaf Gordon。

This sed program was built with SELinux support.
SELinux is disabled on this system.

GNU sed home page: <https://www.gnu.org/software/sed/>.
General help using GNU software: <https://www.gnu.org/gethelp/>.
E-mail bug reports to: <bug-sed@gnu.org>.
```



## Installation

Open the [hiragana_to_latin.py](https://github.com/KawaneRio/japanese-custom-emoji-naming-convention/blob/main/hiragana_to_latin.py) and edit Line 4 so it matches with the location of Japanese-Latin_Conversion_Table2, which should be in the same directory.

After that, run the following command from the same directory:

```
echo "そのカスタム絵文字いつ使うんだよ…" | jumanpp --force-single-path | sed -n 's/[^ ]* \([^ ]*\) .*/\1_/p' | tr -d '\n' | python3 hiragana_to_latin.py
```

You should see 

```
sono_kasutamu_e_mozi_itu_tukau_nda_yo__ooo
```

as the output.


Edit the content inside `echo "そのカスタム絵文字いつ使うんだよ…"` to get the transcription for Japanese emoji names in ASCII-compatible, lowercase latin.


## Issues

This repository is not being actively maintained and exists here for archival purposes only. In other words, the developer (@KawaneRio) is not actively maintaining this code.

However, you are still free to submit Issues at https://github.com/KawaneRio/japanese-custom-emoji-naming-convention/issues . 


## License

[MIT-0](https://github.com/aws/mit-0)




## Citation

The following information may be useful when citing this work.

```
@software{kawanerio_japanese-custom-emoji-naming-convention_2023,
	title = {japanese-custom-emoji-naming-convention},
	rights = {{MIT}-0},
	url = {https://github.com/KawaneRio/japanese-custom-emoji-naming-convention/tree/main},
	abstract = {japanese-custom-emoji-naming-convention is a bash command + python script that converts Japanese echo text into a string of {ASCII}-compatible lowercase latin. The naming convention is based on the Nihonsiki Romanization System for strict transliteration of Japanese. ({ISO} 3602 Strict)},
	version = {v1.0.0},
	author = {{川音リオ@KawaneRio}},
	date = {2023-10-06},
}
```
