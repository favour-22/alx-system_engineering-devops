  import json
  import urllib.request
  import sys

  # Function to get employee name
  def get_employee_name(employee_id):
          url = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)
              response = urllib.request.urlopen(url)
                  data = json.loads(response.read())
                      return data['name']

                  # Function to get employee's tasks
                  def get_employee_tasks(employee_id):
                          url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id)
                              response = urllib.request.urlopen(url)
                                  data = json.loads(response.read())
                                      return data

                                  if len(sys.argv) < 2:
                                          print("Error: Please provide an employee ID as an argument.")
                                              sys.exit(1)

                                              employee_id = int(sys.argv[1])

                                              employee_name = get_employee_name(employee_id)
                                              employee_tasks = get_employee_tasks(employee_id)

                                              completed_tasks = [task for task in employee_tasks if task['completed'] == True]
                                              total_tasks = len(employee_tasks)

                                              print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
                                              for task in completed_tasks:
                                                      print("\t {}".format(task['title']))

