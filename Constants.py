class NumConst():
    countDataStr = 3
    countColumnRes = 4

class StrConst():
    сolumnNameFun = "Функция ПО"
    columnNameRes = "Результат функции"
    columnByte = "Байты"
    columnLocByte = "Положение байтов (с 0)"

class StrRetConts():
    retGood = "good"
    retBat = "bad"

class msgConfirm():
    addMethod = "Метод добавлен"
    setReleaseMethod = "Метод реализован"
    loadFile = "Файл загружен"
    saveFile = "Файл сохранен"
    changeMethod = "Переход между методами осуществлен"
    successCalc = "Вычисление прошло успешно"
    saveMethod = "Метод сохранен"
    saveMethods = "Методы сохранены"
    delMethod = "Метод удален"
    delMethods = "Методы удалены"
    typeMethod = "Тип метода доступен"

class msgError():
    addMethod = "Ошибка при добавлении метода"
    loadFile = "Ошибка при загрузке файла"
    saveFile = "Ошибка при сохранении файла"
    changeMethod = "Ошибка при переходе между методами"
    successCalc = "Ошибка при вычислении"
    saveMethod = "Ошибка при сохранении метода"
    saveMethods = "Ошибка сохранения всех методов"
    delMethod = "Ошибка при удалении метода"
    delMethods = "Ошибка удаления всех методов"
    typeMethod = "Ошибка при выборе типа"

class msgWarning():
    formatMethod = "Неверный формат метода"
    formatResData = "Неверный формат результирующих данных"
    formatData = "Неверный формат данных"
    formatFactory = "Неверный формат фабрики методов"
    noMethods = "Нету методов"
    noPrevMethod = "Нету предыдущего метода"
    noNextMethod = "Нету следующего метода"
    noThisMethod = "Нету текущего метода"
    toMachMethods = "Нету такого количество методов"
    noFileLoad = "Не выбран файл для работы"
    noReleaseMethod = "Данный метод не реализован"

class msgChgNum():
    badPosition = "Ошибка: данного адреса не обнаружено"
    badHexNum = "Ошибка: число не является шестнадцетиричным"
    emptyField = "Ошибка: пустое поле"
    confirmChg = "Изменение прошло успешно"
    confirmCancelChg = "Откат прошел успешно"
    confirmFind = "Байт найден"
    badAction = "Произвести действие не удалось"

class typeMethod():
    typeCheck = "Проверка"
    typeCheckId = 0
    typeBruteForce = "Перебор"
    typeBruteForcekId = 1
    typeRandom = "Рандомизация"
    typeRandomId = 2
    typeCompBase = "Сравнение с исходным"
    typeCompBaseId = 3

class jsonWord():
    method = "method"
    name = "name"
    type = "type"

    mCheck = "MethodCheck"
    mBruteForce = "MBruteForce"
    mRand = "MRand"
    mCompBase = "MCompBase"

    mTimeSleep='timeSleep'
    mPosStart='posStart'
    mPosEnd='posEnd'
    mCountProc='countProc'
    mTimeWait='timeWait'
    mLstPosition='lstPosition'
    mCountRandom='countRandom'
    mCountForce='countForce'

    readCfg = 'readCfg'
    readCfgMethods = 'methods'
    readCfgFiles = 'readFiles'
    readCfgChgVal = 'chgVal'

    testFile='testFile'
    execFile='execFile'
    endResFile='endResFile'

    configName='openCfg.json'

    db = 'db'
    dbName = 'name'
    dbHost = 'host'
    dbPosrt = 'port'
    dbUser = 'user'
    dbPsw = 'password'

    mail = 'mail'
    mailSmtp = 'mailSmtp'
    mailLgn = 'lgn'
    mailPsw = 'pswd'
    userMail = 'userMail'

class styles():
    lblStyleGood = "QLabel { color : green; }"
    lblStyleBad = "QLabel { color : red; }"
