let displayValue = '0'

const updateDisplay = () => {
    document.getElementById('inputCal').value = displayValue
}

const getInputValue = () => {
    return document.getElementById('inputCal').value
}

const input = (num) => {
    if (displayValue === '0') {
        displayValue = num
    } else {
        displayValue += num
    }

    updateDisplay()
}

const clearInput = () => {
    document.getElementById('inputCal').value = '0'
    displayValue = '0'
}

const square = (num) => {
    let x = document.getElementById('inputCal').value
    document.getElementById('inputCal').value = (x * x)
}

const percentage = () => {
    const num = document.getElementById('inputCal').value
    document.getElementById('inputCal').value = (num * 0.01)
}

const plusminus = () => {
    let x = getInputValue()
    document.getElementById('inputCal').value = -x
}


const calculate = () => {
    try {
        let inputToEval = getInputValue()
        let result = eval(inputToEval)

        displayValue += "\n=" + result
        updateDisplay()

    } catch (error) {
        displayValue = '\nError'
        updateDisplay()
    }
}