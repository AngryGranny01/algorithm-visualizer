from app.logic.sorting.bubble_sort_stepper import BubbleSortStepper

def test_bubble_sort():
    arr = [5, 3, 8, 4, 2]
    stepper = BubbleSortStepper(arr)

    while not stepper.is_sorted():
        stepper.step()

    assert stepper.arr == sorted(arr)
    assert len(stepper.get_steps()) > 0
