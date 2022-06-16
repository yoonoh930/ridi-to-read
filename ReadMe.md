# Ridi-to-Read

This project is to help convert the ridibooks highlights drag-and-drop format to csv format for the readwise csv import format.

## How to use

```shell
python3 main.py name_of_the_file -t "Book Title" -a "Author Name"
```

## Format of the text file

It should be copied such that 

```
Highlights

[Note]

Date stamp
```

like

```
죽음은 모든 것을 끝내며 따라서 포괄적인 결론이다

2021.01.31.

그의 삶이 끝난 후 그가 지구상에 체류했음을 말해 주는 흔적은 강물에 던져진 돌이 수면에 남기는 흔적만큼도 못 될지도 모른다

2021.01.31.

그리고 그 모든 것 뒤에는 모험과 영웅 같은 것에 대한 열렬한 동경이 자리하고 있어

2021.01.31.
```

