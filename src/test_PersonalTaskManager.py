import pytest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch, MagicMock
from PersonalTaskManager import TaskManager

@pytest.fixture
def app():
    root = tk.Tk()
    app = TaskManager(root)
    yield app
    root.destroy()

def test_add_task(app):
    app.task_entry.insert(0, "Test Task")
    app.add_task()
    assert app.task_listbox.size() == 1
    assert app.task_listbox.get(0) == "Test Task"

@patch('tkinter.messagebox.showwarning')
def test_add_empty_task(mock_showwarning, app):
    app.task_entry.delete(0, tk.END)
    app.add_task()
    mock_showwarning.assert_called_once_with("Warning", "You must enter a task.")
    assert app.task_listbox.size() == 0

def test_delete_task(app):
    app.task_entry.insert(0, "Test Task")
    app.add_task()
    app.task_listbox.select_set(0)
    app.delete_task()
    assert app.task_listbox.size() == 0

@patch('tkinter.messagebox.showwarning')
def test_delete_task_no_selection(mock_showwarning, app):
    app.delete_task()
    mock_showwarning.assert_called_once_with("Warning", "You must select a task to delete.")

def test_mark_complete(app):
    app.task_entry.insert(0, "Test Task")
    app.add_task()
    app.task_listbox.select_set(0)
    app.mark_complete()
    assert app.task_listbox.size() == 1
    assert app.task_listbox.get(0) == "Test Task - Completed"

@patch('tkinter.messagebox.showwarning')
def test_mark_complete_no_selection(mock_showwarning, app):
    app.mark_complete()
    mock_showwarning.assert_called_once_with("Warning", "You must select a task to mark as complete.")
