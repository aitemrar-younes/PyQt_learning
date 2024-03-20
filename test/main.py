from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Projects")
        self.setGeometry(100, 100, 800, 600)

        self.tree_widget = QTreeWidget()
        self.setCentralWidget(self.tree_widget)

        self.tree_widget.setHeaderLabels(["User/Project Name", "Project ID", "Project Date"])

        # Dummy data (replace with your actual data)
        users_projects = {
            "User1": [
                {"name": "Project1", "id": 1, "date": "2022-01-01"},
                {"name": "Project2", "id": 2, "date": "2022-02-15"}
            ],
            "User2": [
                {"name": "Project3", "id": 3, "date": "2022-03-10"},
                {"name": "Project4", "id": 4, "date": "2022-04-20"},
                {"name": "Project5", "id": 5, "date": "2022-05-05"}
            ],
            "User3": [
                {"name": "Project6", "id": 6, "date": "2022-06-30"}
            ]
        }

        # Populate the tree widget with users and their projects
        for user, projects in users_projects.items():
            user_item = QTreeWidgetItem([user])
            for project in projects:
                project_item = QTreeWidgetItem([
                    project["name"],
                    str(project["id"]),
                    project["date"]
                ])
                user_item.addChild(project_item)
            # Collapse user item initially
            self.tree_widget.addTopLevelItem(user_item)
            self.tree_widget.collapseItem(user_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
