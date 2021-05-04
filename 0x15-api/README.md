<p align="center">
    <img alt="0x15-api" src="https://www.planningpme.es/img/planningpme-api.jpg?dc=202011051200" />
</p>
<h1 align="center">
    API
</h1>

## 🧐 Learning Objects

- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

## 🛠 TOOLS

- Any text editor, VI, VIM , EMACS
- Your servers with Facts

## 📝 FILES

<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Directory</th>
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
  <td>0-gather_data_from_an_API.py</td>
  <td>Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-export_to_CSV.py</td>
  <td>Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-export_to_JSON.py </td>
  <td>Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json

</td>
</tr>
<tr>
  <td>3</td>
  <td> 3-dictionary_of_list_of_dictionaries.py</td>
  <td>Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json

</td>
</tr>
</td>
</tr>

</tbody>
</table>

## _BY_ @Giraluna1
