const symbols = ["🍒", "🍋", "🍇", "🍉", "⭐", "🔔", "7️⃣", "🐅"];
const reels = [];
const reelContainers = [];

// Configuração de pagamento com multiplicadores muito mais altos
const paytable = {
  "🐅": { 3: 100, 4: 500, 5: 2500 },   // Tigre - símbolo premium (MUITO ALTO)
  "7️⃣": { 3: 75, 4: 300, 5: 1500 },    // Sete - símbolo alto
  "⭐": { 3: 50, 4: 200, 5: 1000 },     // Estrela - símbolo alto
  "🔔": { 3: 40, 4: 150, 5: 750 },      // Sino - símbolo médio
  "🍉": { 3: 30, 4: 120, 5: 600 },      // Melancia - símbolo médio
  "🍇": { 3: 25, 4: 100, 5: 500 },      // Uva - símbolo baixo
  "🍋": { 3: 20, 4: 80, 5: 400 },       // Limão - símbolo baixo
  "🍒": { 2: 5, 3: 15, 4: 60, 5: 300 }  // Cereja - paga até com 2 símbolos
};

// Probabilidades dos símbolos (peso para sorteio) - Mais balanceado
const symbolWeights = {
  "🍒": 20,  // Comum
  "🍋": 18,
  "🍇": 16,
  "🍉": 14,
  "🔔": 12,
  "⭐": 10,
  "7️⃣": 7,
  "🐅": 3    // Menos raro
};

// Configuração de linhas de pagamento
const paylines = [
  [1, 1, 1, 1, 1], // Linha do meio
  [0, 0, 0, 0, 0], // Linha superior
  [2, 2, 2, 2, 2], // Linha inferior
  [0, 1, 2, 1, 0], // V
  [2, 1, 0, 1, 2], // V invertido
  [0, 0, 1, 2, 2], // Escada desc
  [2, 2, 1, 0, 0], // Escada asc
  [1, 0, 0, 0, 1], // W
  [1, 2, 2, 2, 1], // W invertido
  [0, 1, 0, 1, 0], // Zigue-zague
  [2, 1, 2, 1, 2], // Zigue-zague inv
  [1, 0, 1, 0, 1], // Alternado
  [1, 2, 1, 2, 1], // Alternado inv
  [0, 0, 2, 0, 0], // Diamante
  [2, 2, 0, 2, 2], // Diamante inv
  [0, 1, 1, 1, 0], // Teto
  [2, 1, 1, 1, 2], // Chão
  [1, 0, 2, 0, 1], // X
  [1, 2, 0, 2, 1], // X invertido
  [0, 2, 1, 2, 0]  // Borboleta
];

for (let i = 1; i <= 5; i++) {
  const reel = document.getElementById("reel" + i);
  const container = reel.querySelector('.reel-container');
  reels.push(reel);
  reelContainers.push(container);
}

let saldo = 1000;
let isSpinning = false;
let currentBet = 5;
let activeLinesCount = 20;

const spinBtn = document.getElementById("spin-btn");
const maxBetBtn = document.getElementById("max-bet-btn");
const betInput = document.getElementById("bet");
const msg = document.getElementById("mensagem");
const tigre = document.getElementById("tigre");
const paylinesDisplay = document.getElementById("paylines");
const jackpotText = document.getElementById("jackpot-text");
const canvas = document.getElementById("particles");
const spinOverlay = document.getElementById("spin-animation-overlay");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

function updateSaldo() {
  document.getElementById("saldo").textContent = `Saldo: R$ ${saldo.toFixed(2)}`;
}

function getRandomSymbol() {
  const totalWeight = Object.values(symbolWeights).reduce((sum, weight) => sum + weight, 0);
  let random = Math.random() * totalWeight;
  
  for (const [symbol, weight] of Object.entries(symbolWeights)) {
    random -= weight;
    if (random <= 0) return symbol;
  }
  return symbols[0];
}

function initializeReels() {
  reelContainers.forEach(container => {
    container.innerHTML = '';
    for (let i = 0; i < 15; i++) {
      const symbol = document.createElement('div');
      symbol.className = 'symbol';
      symbol.textContent = getRandomSymbol();
      symbol.style.top = `${i * 93.33}px`;
      container.appendChild(symbol);
    }
  });
}

function animateReel(container, finalSymbols, delay) {
  return new Promise(resolve => {
    setTimeout(() => {
      container.style.transition = 'none';
      container.style.transform = 'translateY(0)';
      
      const newSymbols = [];
      for (let i = 0; i < 20; i++) {
        newSymbols.push(getRandomSymbol());
      }
      newSymbols.push(...finalSymbols);
      
      container.innerHTML = '';
      newSymbols.forEach((sym, i) => {
        const div = document.createElement('div');
        div.className = 'symbol';
        div.textContent = sym;
        div.style.top = `${i * 93.33}px`;
        container.appendChild(div);
      });
      
      container.offsetHeight;
      
      const duration = 2000 + delay * 0.5; // Duração variável
      container.style.transition = `transform ${duration}ms cubic-bezier(0.25, 0.1, 0.25, 1)`;
      container.style.transform = `translateY(-${20 * 93.33}px)`;
      
      setTimeout(() => {
        container.style.transition = 'none';
        resolve();
      }, duration);
    }, delay);
  });
}

function calculateWinnings(results) {
  let totalWin = 0;
  const winningLines = [];
  const winningPositions = [];
  let bestWin = { symbol: '', count: 0, multiplier: 0.4 };

  // Verificar cada linha de pagamento
  paylines.slice(0, activeLinesCount).forEach((line, lineIndex) => {
    const lineSymbols = line.map((row, col) => results[col][row]);
    
    // Contar símbolos consecutivos da esquerda
    let consecutiveCount = 1;
    const firstSymbol = lineSymbols[0];
    
    for (let i = 1; i < lineSymbols.length; i++) {
      if (lineSymbols[i] === firstSymbol) {
        consecutiveCount++;
      } else {
        break;
      }
    }
    
    // Verificar se há pagamento (incluindo 2 símbolos para cerejas)
    const minSymbols = firstSymbol === "🍒" ? 2 : 3;
    if (consecutiveCount >= minSymbols && paytable[firstSymbol]) {
      const multiplier = paytable[firstSymbol][consecutiveCount] || 0;
      if (multiplier > 0) {
        const lineWin = (currentBet / activeLinesCount) * multiplier;
        totalWin += lineWin;
        winningLines.push({
          line: lineIndex + 1,
          symbol: firstSymbol,
          count: consecutiveCount,
          win: lineWin,
          multiplier: multiplier
        });
        
        // Marcar posições vencedoras
        for (let i = 0; i < consecutiveCount; i++) {
          winningPositions.push({ col: i, row: line[i] });
        }
        
        if (multiplier > bestWin.multiplier) {
          bestWin = { symbol: firstSymbol, count: consecutiveCount, multiplier: multiplier };
        }
      }
    }
  });

  // Bônus especial: Tela cheia de tigres - MULTIPLICADORES ÉPICOS
  const allSymbols = results.flat();
  const tigreCount = allSymbols.filter(s => s === '🐅').length;
  
  if (tigreCount === 15) {
    totalWin += currentBet * 5000; // Jackpot MEGA (5000x)
    winningLines.push({ line: 'JACKPOT', symbol: '🐅', count: 15, win: currentBet * 5000, multiplier: 5000 });
  } else if (tigreCount >= 10) {
    totalWin += currentBet * 1000; // Bonus grande (1000x)
    winningLines.push({ line: 'BONUS', symbol: '🐅', count: tigreCount, win: currentBet * 1000, multiplier: 1000 });
  } else if (tigreCount >= 7) {
    totalWin += currentBet * 250; // Bonus médio (250x)
    winningLines.push({ line: 'BONUS', symbol: '🐅', count: tigreCount, win: currentBet * 250, multiplier: 250 });
  }

  return { totalWin, winningLines, winningPositions, bestWin };
}

function highlightWinningSymbols(winningPositions) {
  reelContainers.forEach((container, colIdx) => {
    const symbols = container.querySelectorAll('.symbol');
    symbols.forEach((symbol, rowIdx) => {
      const isWinning = winningPositions.some(pos => 
        pos.col === colIdx && pos.row === (rowIdx - 20)
      );
      if (isWinning) symbol.classList.add('winning');
    });
  });
}

function displayWinMessage(totalWin, winningLines, bestWin) {
  if (totalWin <= 0) {
    msg.textContent = "😿 Que pena! Tente novamente...";
    msg.style.color = "#ff6b6b";
    return;
  }

  const winRatio = totalWin / currentBet;
  
  if (winRatio >= 1000) {
    msg.innerHTML = `🎰 JACKPOT ÉPICO! 🎰<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#FFD700";
    tigre.style.display = "block";
    jackpotText.style.display = "block";
  } else if (winRatio >= 500) {
    msg.innerHTML = `🔥 VITÓRIA LENDÁRIA! 🔥<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#FF4500";
    tigre.style.display = "block";
    jackpotText.style.display = "block";
  } else if (winRatio >= 100) {
    msg.innerHTML = `🎉 MEGA VITÓRIA! 🎉<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#FFD700";
    tigre.style.display = "block";
  } else if (winRatio >= 50) {
    msg.innerHTML = `⭐ GRANDE VITÓRIA! ⭐<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#FFA500";
    tigre.style.display = "block";
  } else if (winRatio >= 20) {
    msg.innerHTML = `✨ Super Vitória! ✨<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#90EE90";
  } else if (winRatio >= 5) {
    msg.innerHTML = `💰 Boa vitória! 💰<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#90EE90";
  } else {
    msg.innerHTML = `🎯 Parabéns! 🎯<br>Ganhou R$ ${totalWin.toFixed(2)} (${winRatio.toFixed(1)}x)!`;
    msg.style.color = "#90EE90";
  }

  // Mostrar detalhes das linhas vencedoras
  if (winningLines.length > 0) {
    const linesText = winningLines.map(line => 
      `L${line.line}: ${line.symbol} x${line.count} (${line.multiplier}x)`
    ).join(", ");
    paylinesDisplay.textContent = `Linhas: ${linesText}`;
  }
}

// Função principal de giro
async function spin() {
  if (isSpinning) return;

  currentBet = Math.min(Math.max(parseFloat(betInput.value) || 5, 1), saldo);
  
  // Validação rigorosa de aposta
  if (currentBet <= 0) {
    msg.textContent = "💸 Valor de aposta inválido! Mínimo R$ 1,00";
    msg.style.color = "#ff4444";
    betInput.value = "1.00";
    return;
  }
  
  if (currentBet > saldo) {
    msg.textContent = "💸 Saldo insuficiente para esta aposta!";
    msg.style.color = "#ff4444";
    betInput.value = saldo.toFixed(2);
    return;
  }

  if (saldo < 1) {
    msg.textContent = "💸 Saldo insuficiente! Você precisa de pelo menos R$ 1,00";
    msg.style.color = "#ff4444";
    return;
  }

  isSpinning = true;
  saldo -= currentBet;
  updateSaldo();

  msg.textContent = "🎰 Girando...";
  msg.style.color = "#FFD700";
  paylinesDisplay.textContent = "";
  tigre.style.display = "none";
  jackpotText.style.display = "none";
  spinBtn.disabled = true;
  maxBetBtn.disabled = true;
  
  if (spinOverlay) spinOverlay.classList.add('active');

  document.querySelectorAll('.symbol.winning').forEach(sym => {
    sym.classList.remove('winning');
  });

  const results = [];
  const animations = [];

  for (let i = 0; i < 5; i++) {
    const reelResult = [];
    for (let j = 0; j < 3; j++) {
      reelResult.push(getRandomSymbol());
    }
    results.push(reelResult);
    animations.push(animateReel(reelContainers[i], reelResult, i * 200));
  }

  await Promise.all(animations);

  if (spinOverlay) spinOverlay.classList.remove('active');
  
  const { totalWin, winningLines, winningPositions, bestWin } = calculateWinnings(results);
  saldo += totalWin;
  updateSaldo();

  if (winningPositions.length > 0) highlightWinningSymbols(winningPositions);
  displayWinMessage(totalWin, winningLines, bestWin);

  spinBtn.disabled = false;
  maxBetBtn.disabled = false;
  isSpinning = false;
}

// Event listeners
spinBtn.addEventListener("click", spin);

maxBetBtn.addEventListener("click", () => {
  const maxBet = Math.min(100, saldo);
  betInput.value = maxBet.toFixed(2);
  spin();
});

betInput.addEventListener("input", () => {
  let value = parseFloat(betInput.value);
  
  // Validação rigorosa
  if (isNaN(value) || value <= 0) {
    betInput.value = "1.00";
    return;
  }
  
  if (value > saldo) {
    betInput.value = saldo.toFixed(2);
    return;
  }
  
  if (value < 1) {
    betInput.value = "1.00";
    return;
  }
  
  // Arredondar para 2 casas decimais
  betInput.value = value.toFixed(2);
});

document.addEventListener("keydown", (e) => {
  if (e.code === "Space" && !isSpinning) {
    e.preventDefault();
    spin();
  }
});

// Função para mostrar tabela de pagamentos
function showPaytable() {
  console.log("=== TABELA DE PAGAMENTOS (MULTIPLICADORES ALTOS) ===");
  Object.entries(paytable).forEach(([symbol, pays]) => {
    console.log(`${symbol}: 3x = ${pays[3]}x | 4x = ${pays[4]}x | 5x = ${pays[5]}x`);
  });
  console.log("🐅 BÔNUS ESPECIAIS:");
  console.log("15 Tigres = 5000x (JACKPOT ÉPICO)");
  console.log("10+ Tigres = 1000x (GRANDE BÔNUS)");
  console.log("7+ Tigres = 250x (BÔNUS MÉDIO)");
}

// Inicializar
initializeReels();
updateSaldo();

// Mostrar tabela no console para referência
showPaytable();