class NumConst():
    countDataStr = 3
    countColumnRes = 4

class StrConst():
    сolumnNameFun = "Функция ПО"
    columnNameRes = "Результат функции"
    columnByte = "Байты"
    columnLocByte = "Положение байтов (с 0)"
    noUse = "Не используется"

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

    conn = "Подключение удалось"

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

    conn = "Подключение не удалось"

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
    typeMoreOneRand = "Множественный рандом"
    typeMoreOneRandId = 4
    typeReverse = "Реверс проверка"
    typeReverseId = 5

class icons():
    wayIconPackage = 'resources/icons/'
    btnPackage = 'btn/'
    calcThisMethod = wayIconPackage + btnPackage + 'calcThisMethod.png'
    prevMethod = wayIconPackage + btnPackage + 'prevMethod.png'
    nextMethod = wayIconPackage + btnPackage + 'nextMethod.png'
    currMethod = wayIconPackage + btnPackage + 'currentMethod.png'
    addMethod = wayIconPackage + btnPackage + 'addMethod.png'
    editMethod = wayIconPackage + btnPackage + 'editMethod.png'
    delMethod = wayIconPackage + btnPackage + 'delMethod.png'
    addByteChange = wayIconPackage + btnPackage + 'addByteChange.png'
    delByteChange = wayIconPackage + btnPackage + 'delByteChange.png'
    searchByteChange = wayIconPackage + btnPackage + 'searchByteChange.png'
    startByteChange = wayIconPackage + btnPackage + 'startByteChange.png'
    confirmByteChange = wayIconPackage + btnPackage + 'confirmByteChange.png'
    all = wayIconPackage + btnPackage + 'all.png'
    confirmAllByteChanges = wayIconPackage + btnPackage + 'confirmAllByteChange.png'
    delAllByteChanges = wayIconPackage + btnPackage + 'delAllByteChange.png'
    delAllMethods = wayIconPackage + btnPackage + 'delAllMethods.png'
    searchAllByteChanges = wayIconPackage + btnPackage + 'searchAllByteChange.png'
    startAllByteChanges = wayIconPackage + btnPackage + 'startAllByteChange.png'

class jsonWord():
    method = "method"
    name = "name"
    type = "type"

    mCheck = "MethodCheck"
    mBruteForce = "MBruteForce"
    mRand = "MRand"
    mCompBase = "MCompBase"
    mMoreOneRand = "MMoreOneRand"
    mReverse = "MReverse"

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

class idConnWnd():
    idDB = 0
    idMail = 1

class connDB():
    lbl0 = 'Название базы'
    lbl1 = 'Пользователь базы'
    lbl2 = 'Пароль к базе'
    lbl3 = 'Хост базы'
    lbl4 = 'Порт базы'

class connMail():
    lbl0 = 'smtp сервер (пример: smtp.mail.ru)'
    lbl1 = 'Логин почты отправки'
    lbl2 = 'Пароль почты отправки'
    lbl3 = 'Почта, на которую будет производиться отправка'
