import pytest
from unittest.mock import MagicMock, patch
from PersonalTaskManager import TaskManager

@pytest.fixture
def app():
    with patch('PersonalTaskManager.tk.Tk') as MockTk:
        root = MockTk()
        app = TaskManager(root)
        yield app

def test_add_task(app):
    app.task_entry.get = MagicMock(return_value="Test Task")
    app.task_entry.delete = MagicMock()
    app.task_listbox.insert = MagicMock()
    
    app.add_task()
    
    app.task_listbox.insert.assert_called_once_with('end', "Test Task")
    app.task_entry.delete.assert_called_once_with(0, 'end')

@patch('PersonalTaskManager.messagebox.showwarning')
def test_add_empty_task(mock_showwarning, app):
    app.task_entry.get = MagicMock(return_value="")
    app.task_entry.delete = MagicMock()
    app.task_listbox.insert = MagicMock()
    
    app.add_task()
    
    mock_showwarning.assert_called_once_with("Warning", "You must enter a task.")
    app.task_listbox.insert.assert_not_called()

def test_delete_task(app):
    app.task_listbox.curselection = MagicMock(return_value=[0])
    app.task_listbox.delete = MagicMock()
    
    app.delete_task()
    
    app.task_listbox.delete.assert_called_once_with(0)

@patch('PersonalTaskManager.messagebox.showwarning')
def test_delete_task_no_selection(mock_showwarning, app):
    app.task_listbox.curselection = MagicMock(return_value=[])
    
    app.delete_task()
    
    mock_showwarning.assert_called_once_with("Warning", "You must select a task to delete.")

def test_mark_complete(app):
    app.task_listbox.curselection = MagicMock(return_value=[0])
    app.task_listbox.get = MagicMock(return_value="Test Task")
    app.task_listbox.delete = MagicMock()
    app.task_listbox.insert = MagicMock()
    
    app.mark_complete()
    
    app.task_listbox.delete.assert_called_once_with(0)
    app.task_listbox.insert.assert_called_once_with('end', "Test Task - Completed")

@patch('PersonalTaskManager.messagebox.showwarning')
def test_mark_complete_no_selection(mock_showwarning, app):
    app.task_listbox.curselection = MagicMock(return_value=[])
    
    app.mark_complete()
    
    mock_showwarning.assert_called_once_with("Warning", "You must select a task to mark as complete.")
