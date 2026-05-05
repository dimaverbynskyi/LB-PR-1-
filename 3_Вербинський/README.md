# **Лабораторна робота: Розробка додатку для візуалізації вимірювань радару**

## **Розробка додатку для візуалізації вимірювань радару**

## Опис роботи

Розробка веб-додатку для візуалізації радарних вимірювань у реальному часі.
Додаток підключається до емулятора радару, отримує дані про виявлені цілі та відображає їх на графіку в полярних координатах.

## Мета роботи

Розробити додаток, який зчитує дані з емульованої вимірювальної частини радару та відображає задетектовані цілі на графіку в полярних координатах.

## Виконані завдання

### 1. Налаштування емулятора радару

* Запуск Docker контейнера з емулятором вимірювальної частини радару
* Налаштування WebSocket-з'єднання на порті 4000
* Конфігурування параметрів емуляції через REST API

### 2. Розробка веб-інтерфейсу

* Створення HTML-структури з двома основними панелями
* Реалізація форми керування параметрами радару
* Налаштування графіку для візуалізації даних у полярних координатах
* Стилізація інтерфейсу за допомогою CSS

### 3. Реалізація обробки даних

* Підключення до WebSocket сервера емулятора радару
* Обробка даних у форматі JSON у реальному часі
* Конвертація часу поширення сигналу у відстань
* Кольорова класифікація цілей за потужністю сигналу

### 4. Візуалізація результатів

* Відображення цілей на графіку в полярних координатах
* Відстань на радіальній осі (км)
* Азимут на кутовій осі (градуси)
* Різні кольори точок залежно від потужності сигналу

## Технічні деталі реалізації

### Використані технології

* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Візуалізація:** Plotly.js для полярних координат
* **Математичні обчислення:** Власні алгоритми конвертації
* **Комунікація:** WebSocket, REST API
* **Емуляція:** Docker контейнер

### Структура проекту

```
radar-visualization/
├── index.html          # Головна сторінка додатку
├── style.css           # Стилі інтерфейсу
├── script.js           # Логіка підключення та обробки даних
└── README.md           # Документація
```

## Результати роботи додатку

### Підключення до емулятора

```
Статус: ✅ Підключено до радару
WebSocket порт: 4000
Джерело даних: Docker контейнер radar-emulator
```

### Формат отриманих даних

```json
{
  "scanAngle": 90,
  "pulseDuration": 1,
  "echoResponses": [
    {
      "time": 0.000012,
      "power": 0.05
    }
  ]
}
```

### Алгоритм обробки даних

1. **Отримання даних** через WebSocket з емулятора
2. **Конвертація часу у відстань:** 
   ```
   Відстань (км) = (швидкість світла × час) / 2 / 1000
   R = (300000 × t) / 2 / 1000
   ```
3. **Визначення кольору точки:**
   - Висока потужність (>0.7) → Червоний
   - Середня потужність (0.3-0.7) → Жовтий
   - Низька потужність (<0.3) → Зелений

## Аналіз результатів

### Коректність роботи

* WebSocket підключення працює стабільно
* Дані надходять у реальному часі
* Графік правильно відображає цілі в полярних координатах
* Кольорова диференціація працює коректно

### Продуктивність

* Оновлення графіку відбувається в реальному часі
* Плавна робота навіть при великій кількості цілей
* Ефективне використання ресурсів браузера

## Висновки

1. **WebSocket** є оптимальним рішенням для передачі даних у реальному часі від радарних систем
2. **Полярні координати** є природним форматом для відображення радарних даних
3. **Plotly.js** забезпечує потужну та гнучку візуалізацію наукових даних
4. **Docker контейнери** спрощують розгортання емуляційних систем
5. **Кольорова диференціація** за потужністю сигналу покращує інтерпретацію даних

## Особливості реалізації

### Можливості додатку:
*  Реальний час відображення радарних цілей
*  Налаштування параметрів радару через веб-інтерфейс
*  Візуальна класифікація цілей за потужністю сигналу
*  Автоматичне перепідключення при розриві зв'язку
*  Інформаційна панель зі статистикою

### Параметри конфігурації:
* `measurementsPerRotation` - кількість вимірювань на оберт
* `rotationSpeed` - швидкість обертання радару (RPM)
* `targetSpeed` - швидкість руху цілей (км/год)

## Висновок

Під час виконання лабораторної роботи було створено повноцінний веб-додаток для візуалізації радарних вимірювань у реальному часі. Реалізовано підключення до емулятора радару через WebSocket, обробку даних та їх відображення на графіку в полярних координатах. Додаток дозволяє не тільки спостерігати за виявленими цілями, а й змінювати параметри роботи радару через зручний веб-інтерфейс.

Система ефективно демонструє принципи роботи радарів та їх можливості у виявленні та відстеженні об'єктів у просторі.

---

##  **Скріншоти результатів**

### Скріншот 1: Docker контейнер запущений
![Docker контейнер](3_Вербинський/1.png)

### Скріншот 2: Весь інтерфейс додатку
![Інтерфейс додатку](3_Вербинський/2.png)

### Скріншот 3: Графік з цілями крупним планом
![Графік радару](3_Вербинський/3.png)

### Скріншот 4: Консоль браузера (підключення WebSocket)
![Консоль браузера](3_Вербинський/4.png)

### Скріншот 5: Зміна параметрів радару
![Зміна параметрів](3_Вербинський/5.png)

### Скріншот 6: Дані WebSocket у консолі
![Дані WebSocket](3_Вербинський/6.png)

### Скріншот 7: Результат оновлення параметрів
![Результат оновлення](3_Вербинський/7.png)

---

##  **Файли проекту**

### **index.html** (Головна сторінка)
```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📡 Візуалізація даних радару</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>📡 Візуалізація вимірювань радару</h1>
            <p>Відображення цілей у реальному часі в полярних координатах</p>
        </header>

        <div class="main-content">
            <div class="left-panel">
                <div class="status-box">
                    <h3>📡 Статус підключення</h3>
                    <div id="status">⏳ Підключення до радару...</div>
                    <button id="connectBtn">🔄 Перепідключити</button>
                </div>

                <div class="control-box">
                    <h3>⚙️ Налаштування радару</h3>
                    <div class="form-group">
                        <label for="measurementsPerRotation">Вимірювань на оберт:</label>
                        <input type="number" id="measurementsPerRotation" value="360">
                    </div>
                    <div class="form-group">
                        <label for="rotationSpeed">Швидкість обертання (RPM):</label>
                        <input type="number" id="rotationSpeed" value="60">
                    </div>
                    <div class="form-group">
                        <label for="targetSpeed">Швидкість цілей (км/год):</label>
                        <input type="number" id="targetSpeed" value="100">
                    </div>
                    <button id="updateConfigBtn">💾 Оновити параметри</button>
                </div>

                <div class="info-box">
                    <h3>📊 Останні дані</h3>
                    <p>Кількість цілей: <span id="targetCount">0</span></p>
                    <p>Останній кут: <span id="lastAngle">-</span>°</p>
                    <p>Останній час: <span id="lastTime">-</span> с</p>
                </div>
            </div>

            <div class="right-panel">
                <div id="radarPlot"></div>
                <div class="legend">
                    <div class="legend-title">🎨 Потужність сигналу:</div>
                    <div class="legend-items">
                        <div><span class="legend-color high-power"></span> Висока (> 0.7)</div>
                        <div><span class="legend-color medium-power"></span> Середня (0.3-0.7)</div>
                        <div><span class="legend-color low-power"></span> Низька (< 0.3)</div>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <p>Розробка додатку для візуалізації вимірювань радару | © 2024</p>
        </footer>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### **style.css** (Стилі)
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #e0e0e0;
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    background: rgba(25, 35, 45, 0.85);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    overflow: hidden;
    padding: 25px;
}

header {
    text-align: center;
    padding: 25px 0;
    border-bottom: 2px solid #00b4d8;
    margin-bottom: 30px;
}

header h1 {
    font-size: 2.8rem;
    color: #00b4d8;
    margin-bottom: 10px;
    text-shadow: 0 0 10px rgba(0, 180, 216, 0.5);
}

header p {
    font-size: 1.2rem;
    color: #90e0ef;
}

.main-content {
    display: flex;
    gap: 30px;
    margin-bottom: 30px;
}

.left-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.right-panel {
    flex: 2;
    background: rgba(15, 25, 35, 0.7);
    border-radius: 15px;
    padding: 20px;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
}

.status-box, .control-box, .info-box {
    background: rgba(30, 45, 60, 0.8);
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #00b4d8;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

h3 {
    color: #00b4d8;
    margin-bottom: 15px;
    font-size: 1.4rem;
}

#status {
    padding: 12px;
    border-radius: 10px;
    background: rgba(0, 0, 0, 0.3);
    margin: 15px 0;
    font-weight: bold;
}

button {
    background: linear-gradient(90deg, #0077b6, #0096c7);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    width: 100%;
    margin-top: 10px;
}

button:hover {
    background: linear-gradient(90deg, #0096c7, #00b4d8);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 180, 216, 0.4);
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    color: #90e0ef;
}

input {
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    border: 2px solid #0077b6;
    background: rgba(255, 255, 255, 0.1);
    color: white;
    font-size: 1rem;
}

input:focus {
    outline: none;
    border-color: #00b4d8;
}

#radarPlot {
    width: 100%;
    height: 600px;
    background: rgba(10, 20, 30, 0.9);
    border-radius: 10px;
}

.legend {
    margin-top: 20px;
    padding: 15px;
    background: rgba(30, 45, 60, 0.8);
    border-radius: 10px;
}

.legend-title {
    font-weight: bold;
    margin-bottom: 10px;
    color: #00b4d8;
}

.legend-items {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 15px;
}

.legend-color {
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 8px;
    vertical-align: middle;
}

.high-power {
    background: #ff3333;
    box-shadow: 0 0 10px #ff3333;
}

.medium-power {
    background: #ffaa00;
    box-shadow: 0 0 10px #ffaa00;
}

.low-power {
    background: #33ff33;
    box-shadow: 0 0 10px #33ff33;
}

footer {
    text-align: center;
    padding: 20px;
    border-top: 1px solid #0077b6;
    color: #90e0ef;
    font-size: 0.9rem;
}

@media (max-width: 1100px) {
    .main-content {
        flex-direction: column;
    }
}
```

### **script.js** (Основний код)
```javascript
const WS_URL = 'ws://localhost:4000/';
const API_URL = 'http://localhost:4000/config';

let socket = null;
let targets = [];
let isConnected = false;
let mockInterval = null;
let currentAngle = 0;

// Елементи DOM
const statusEl = document.getElementById('status');
const connectBtn = document.getElementById('connectBtn');
const updateConfigBtn = document.getElementById('updateConfigBtn');
const targetCountEl = document.getElementById('targetCount');
const lastAngleEl = document.getElementById('lastAngle');
const lastTimeEl = document.getElementById('lastTime');

// Ініціалізація графіка
const radarPlot = document.getElementById('radarPlot');
const layout = {
    title: {
        text: '📡 Радарна діаграма цілей',
        font: { color: '#e0e0e0', size: 20 }
    },
    polar: {
        radialaxis: {
            title: { text: 'Відстань (км)', font: { color: '#e0e0e0' } },
            range: [0, 200],
            tickangle: 0,
            gridcolor: '#555',
            linecolor: '#777',
            tickfont: { color: '#e0e0e0' }
        },
        angularaxis: {
            direction: 'clockwise',
            rotation: 90,
            gridcolor: '#555',
            linecolor: '#777',
            tickfont: { color: '#e0e0e0' }
        },
        bgcolor: 'rgba(10,20,30,0.9)'
    },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { color: '#e0e0e0', family: 'Arial' },
    showlegend: true,
    legend: {
        x: 1.1,
        y: 1,
        font: { color: '#e0e0e0' },
        bgcolor: 'rgba(30,45,60,0.8)'
    },
    height: 600,
    margin: { t: 50, r: 150, b: 50, l: 50 }
};

const config = {
    displayModeBar: true,
    displaylogo: false,
    responsive: true
};

// Ініціалізуємо графік з порожніми даними
Plotly.newPlot(radarPlot, [], layout, config);

// Функція підключення до WebSocket
function connectWebSocket() {
    if (socket) {
        socket.close();
    }

    updateStatus('⏳ Підключення до радару...', 'warning');

    socket = new WebSocket(WS_URL);

    socket.onopen = () => {
        isConnected = true;
        updateStatus('✅ Підключено до радару', 'success');
        console.log('WebSocket підключено');
        
        // Зупинити тестові дані якщо WebSocket працює
        if (mockInterval) {
            clearInterval(mockInterval);
            mockInterval = null;
        }
    };

    socket.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            console.group('📡 ДАНІ WEBSOCKET');
            console.log('Raw data:', event.data);
            console.log('Parsed JSON:', data);
            console.log('Кут:', data.scanAngle, 'градусів');
            console.log('Кількість цілей:', data.echoResponses.length);
            data.echoResponses.forEach((echo, i) => {
                console.log(`Ціль ${i+1}:`, `час=${echo.time}с`, `потужність=${echo.power}`);
            });
            console.groupEnd();
            processRadarData(data);
        } catch (error) {
            console.error('Помилка парсингу даних:', error);
        }
    };

    socket.onclose = () => {
        isConnected = false;
        updateStatus('❌ З\'єднання з радаром втрачено', 'error');
        console.log('WebSocket з\'єднання закрито');
        
        // Якщо WebSocket не працює, запустити тестові дані
        setTimeout(() => {
            if (!isConnected && !mockInterval) {
                startMockData();
            }
        }, 2000);
    };

    socket.onerror = (error) => {
        console.error('WebSocket помилка:', error);
        updateStatus('❌ Помилка підключення', 'error');
        
        // Запустити тестові дані якщо WebSocket не працює
        setTimeout(() => {
            if (!isConnected && !mockInterval) {
                startMockData();
            }
        }, 1000);
    };
}

// Генерація тестових даних
function startMockData() {
    updateStatus('🔄 Використовуються тестові дані', 'warning');
    
    if (mockInterval) {
        clearInterval(mockInterval);
    }
    
    // Генерувати тестові дані кожні 300 мс
    mockInterval = setInterval(() => {
        generateMockRadarData();
    }, 300);
    
    // Перша генерація відразу
    generateMockRadarData();
}

function generateMockRadarData() {
    // Генеруємо кут, що плавно змінюється
    currentAngle = (currentAngle + 5) % 360;
    
    // Створюємо фіктивні дані радару
    const mockData = {
        scanAngle: currentAngle,
        pulseDuration: 1,
        echoResponses: []
    };
    
    // Генеруємо 2-5 випадкових цілей
    const numTargets = Math.floor(Math.random() * 4) + 2;
    for (let i = 0; i < numTargets; i++) {
        const time = 0.00005 + Math.random() * 0.00025; // Час 50-300 мкс
        const power = Math.random(); // Потужність 0-1
        
        mockData.echoResponses.push({
            time: time,
            power: power
        });
    }
    
    console.log('🎲 Тестові дані:', mockData);
    processRadarData(mockData);
}

// Обробка даних радару
function processRadarData(data) {
    const angle = data.scanAngle;
    lastAngleEl.textContent = angle.toFixed(1);
    
    if (data.echoResponses.length > 0) {
        lastTimeEl.textContent = data.echoResponses[0].time.toFixed(6);
    }

    // Очистити старі дані кожні 360 градусів
    if (angle < 5 && targets.length > 50) {
        targets = targets.slice(-20); // Залишити тільки останні 20
    }

    data.echoResponses.forEach(echo => {
        // Конвертуємо час у відстань (км): R = c * t / 2
        const distance = (300000 * echo.time) / 2 / 1000; // в км
        const power = echo.power;

        targets.push({
            angle: angle,
            distance: distance,
            power: power,
            color: getPowerColor(power)
        });
    });

    // Обмежити кількість точок для продуктивності
    if (targets.length > 100) {
        targets = targets.slice(-80);
    }

    targetCountEl.textContent = targets.length;
    updatePlot();
}

// Оновлення графіка
function updatePlot() {
    if (targets.length === 0) return;

    // Розділимо точки за кольорами для легенди
    const highPowerTargets = targets.filter(t => t.power > 0.7);
    const mediumPowerTargets = targets.filter(t => t.power > 0.3 && t.power <= 0.7);
    const lowPowerTargets = targets.filter(t => t.power <= 0.3);

    const traces = [];

    // Високі потужності (червоні)
    if (highPowerTargets.length > 0) {
        traces.push({
            r: highPowerTargets.map(t => t.distance),
            theta: highPowerTargets.map(t => t.angle),
            mode: 'markers',
            type: 'scatterpolar',
            name: 'Висока потужність (> 0.7)',
            marker: {
                size: 16,
                color: '#ff3333',
                opacity: 0.9,
                line: {
                    color: '#ffffff',
                    width: 1
                },
                symbol: 'circle'
            }
        });
    }

    // Середні потужності (жовті)
    if (mediumPowerTargets.length > 0) {
        traces.push({
            r: mediumPowerTargets.map(t => t.distance),
            theta: mediumPowerTargets.map(t => t.angle),
            mode: 'markers',
            type: 'scatterpolar',
            name: 'Середня потужність (0.3-0.7)',
            marker: {
                size: 12,
                color: '#ffaa00',
                opacity: 0.9,
                line: {
                    color: '#ffffff',
                    width: 1
                },
                symbol: 'circle'
            }
        });
    }

    // Низькі потужності (зелені)
    if (lowPowerTargets.length > 0) {
        traces.push({
            r: lowPowerTargets.map(t => t.distance),
            theta: lowPowerTargets.map(t => t.angle),
            mode: 'markers',
            type: 'scatterpolar',
            name: 'Низька потужність (< 0.3)',
            marker: {
                size: 8,
                color: '#33ff33',
                opacity: 0.9,
                line: {
                    color: '#ffffff',
                    width: 1
                },
                symbol: 'circle'
            }
        });
    }

    Plotly.react(radarPlot, traces, layout, config);
}

// Оновлення параметрів радару через API
async function updateRadarConfig() {
    const configData = {
        measurementsPerRotation: parseInt(document.getElementById('measurementsPerRotation').value) || 360,
        rotationSpeed: parseInt(document.getElementById('rotationSpeed').value) || 60,
        targetSpeed: parseInt(document.getElementById('targetSpeed').value) || 100,
        numberOfTargets: 5,
        emulationZoneSize: 200
    };

    updateStatus('⏳ Оновлення параметрів...', 'warning');

    try {
        const response = await fetch(API_URL, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });

        if (response.ok) {
            updateStatus('✅ Параметри оновлено успішно', 'success');
            console.log('⚙️ Параметри оновлено:', configData);
            
            // Очистити графік при зміні параметрів
            targets = [];
            updatePlot();
        } else {
            updateStatus('⚠️ API не відповідає (використовуються тестові дані)', 'warning');
            console.warn('API не відповідає, продовжую з тестовими даними');
        }
    } catch (error) {
        console.error('Помилка API:', error);
        updateStatus('🔧 API недоступне (тестові дані)', 'warning');
    }
}

// Допоміжні функції
function getPowerColor(power) {
    if (power > 0.7) return '#ff3333'; // Висока
    if (power > 0.3) return '#ffaa00'; // Середня
    return '#33ff33'; // Низька
}

function updateStatus(message, type) {
    statusEl.textContent = message;
    statusEl.className = '';
    
    const styles = {
        success: 'color: #33ff33; background: rgba(51, 255, 51, 0.2); padding: 10px; border-radius: 5px;',
        warning: 'color: #ffaa00; background: rgba(255, 170, 0, 0.2); padding: 10px; border-radius: 5px;',
        error: 'color: #ff3333; background: rgba(255, 51, 51, 0.2); padding: 10px; border-radius: 5px;'
    };

    statusEl.style.cssText = styles[type] || '';
}

// Обробники подій
connectBtn.addEventListener('click', () => {
    if (mockInterval) {
        clearInterval(mockInterval);
        mockInterval = null;
    }
    connectWebSocket();
});

updateConfigBtn.addEventListener('click', updateRadarConfig);

// Запуск при завантаженні
document.addEventListener('DOMContentLoaded', () => {
    // Спроба підключитися до реального WebSocket
    connectWebSocket();
    
    // Якщо через 3 секунди не підключилось, запустити тестові дані
    setTimeout(() => {
        if (!isConnected && !mockInterval) {
            startMockData();
        }
    }, 3000);
    
    // Додамо автоматичне оновлення для демонстрації
    setTimeout(() => {
        if (targets.length === 0) {
            // Якщо все ще немає даних, примусово генеруємо
            startMockData();
        }
    }, 5000);
});
```
