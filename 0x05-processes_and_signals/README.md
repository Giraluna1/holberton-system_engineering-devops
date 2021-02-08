#  PROCESSES AND SIGNALS
This project you find several task to learn ssh with linux:

   - What is a PID
   - What is a process
   - How to find a process’ PID
   - How to kill a process
   - What is a signal
   - What are the 2 signals that cannot be ignored


## **FILES**
<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Files</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td></td>
  <td> README.md</td>
  <td>...<td>
</tr>
<tr>
  <td>0</td>
  <td>0-what-is-my-pid</td>
  <td>Write a Bash script that displays its own PID.
</td>
</tr>
<tr>
  <td>1</td>
  <td>1-list_your_processes</td>
  <td>Write a Bash script that displays a list of currently running processes.

Requirements:

    Must show all processes, for all users, including those which might not have a TTY
    Display in a user-oriented format
    Show process hierarchy
</td>
</tr>
<tr>
  <td>2</td>
  <td>2-show_your_bash_pid</td>
  <td>Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

    You cannot use pgrep
    The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
</td>
</tr>
<tr>
  <td>3</td>
  <td>3-until_holberton_school</td>
  <td>Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

    You cannot use ps
</td>
</tr>
<tr>
  <td>4</td>
  <td>4-to_infinity_and_beyond</td>
  <td>Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

    In between each iteration of the loop, add a sleep 2
</td>
</tr>
<tr>
  <td>5</td>
  <td>5-dont_stop_me_now</td>
  <td>We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

    You must use kill


</td>
</tr>
<tr>
  <td>6</td>
  <td>6-stop_me_if_you_can</td>
  <td>Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

    You cannot use kill or killall
</td>
</tr>
<tr>
  <td>7</td>
  <td>7-highlander</td>
  <td>Write a Bash script that displays:

    To infinity and beyond indefinitely
    With a sleep 2 in between each iteration
    I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.
</td>
</tr>
<tr>
  <td>8</td>
  <td>8-beheaded_process</td>
  <td>Write a Bash script that kills the process 7-highlander.
</td>
</tr>


</td>
</tr>
</tbody>
</table>

### _By Giraluna Gomez_
### @Giraluna1