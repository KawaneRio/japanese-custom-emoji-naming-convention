# japanese-custom-emoji-naming-convention
This is a bash command + python script that converts Japanese echo text into a string of ASCII-compatible lowercase latin. The naming convention is based on the [Nihonsiki](https://en.wikipedia.org/wiki/Nihon-shiki_romanization) Romanization System for strict transliteration of Japanese. (See ISO 3602 Strict)

* Prerequisities

** JUMAN++

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
sudo make instal
```

** Python3

You will also need to be able to run `python3`. Try running `python3 --version` on your terminal. Mine looks like this:

```
kawanerio@MoebuntuStudio11:~/jumanpp-1.01$ python3 --version
Python 3.10.12
```

If not installed, try searching "How to install Python3" on the internet. 

** sed

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

* Installation

