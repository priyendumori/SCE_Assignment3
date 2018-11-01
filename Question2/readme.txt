Commands:

1.  cd <path>
    example: cd /home/user/something
             cd something_in_current_directory
             cd ~
             cd .
             cd ..

2.  pwd
    example: pwd

3.  ls <path> or ls
    example: ls 
             ls dir_name
             ls ~

4.  touch <file1 file2 ...>
    example: touch a
             touch a b c
             touch dir1/a dir2/b

5.  head <file1 file2 ....>
    example: head a
             head a b c
             head dir1/a

6.  tail <file1 file2 ....>
    example: tail a
             tail a b c
             tail dir1/a  

7.  tr <chars_to_change chars_to_change_to>
    example: tr abc ABC
             press $ to exit tr
             basic
             BasiC
             pass
             pAss
             $

8.  grep "<pattern>" <<< "<text>"
    example: grep "str" <<< "string"

9.  sed "s/<pattern_to_replace>/<replace_with>/g" <<< "text"
    example: sed "s/ab/ab /g" <<< "ababa"
             ab ab a

10. diff <file1 file2>
    example: diff abc.txt def.txt
