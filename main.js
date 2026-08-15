/**
 * PlantaSanitus🌿 - Interactive Engine
 * Multi-Image Selection, XAI Region Overlay, Dosage Calculator, Shopping Cart, and Voice AI Chatbot
 */

let selectedFiles = [];
let cart = JSON.parse(localStorage.getItem('ps_cart') || '[]');

document.addEventListener('DOMContentLoaded', () => {
  const dropzone = document.getElementById('dropzone');
  const leafInput = document.getElementById('leafInput');
  const previewContainer = document.getElementById('previewContainer');
  const previewGrid = document.getElementById('previewGrid');
  const analyzeBtn = document.getElementById('analyzeBtn');

  const resultPlaceholder = document.getElementById('resultPlaceholder');
  const resultContent = document.getElementById('resultContent');

  updateCartBadge();
  if (window.location.pathname === '/cart') {
    renderCartPage();
  }

  if (dropzone && leafInput) {
    ['dragenter', 'dragover'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
      }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.remove('dragover');
      }, false);
    });

    dropzone.addEventListener('drop', (e) => {
      const files = Array.from(e.dataTransfer.files).filter(f => f.type.startsWith('image/'));
      if (files.length > 0) handleMultiFiles(files);
    });

    dropzone.addEventListener('click', () => leafInput.click());

    leafInput.addEventListener('change', (e) => {
      const files = Array.from(e.target.files).filter(f => f.type.startsWith('image/'));
      if (files.length > 0) handleMultiFiles(files);
    });
  }

  function handleMultiFiles(files) {
    selectedFiles = files.slice(0, 3); // Max 3 images
    previewGrid.innerHTML = '';
    
    selectedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        const div = document.createElement('div');
        div.style.position = 'relative';
        div.innerHTML = `<img src="${e.target.result}" style="width:100%; height:100px; object-fit:cover; border-radius:6px; border:1px solid var(--border-glass);">`;
        previewGrid.appendChild(div);
      };
      reader.readAsDataURL(file);
    });

    previewContainer.style.display = 'block';
    dropzone.style.display = 'none';
    if (analyzeBtn) analyzeBtn.disabled = false;
  }

  if (analyzeBtn) {
    analyzeBtn.addEventListener('click', () => {
      if (selectedFiles.length === 0) return;
      
      analyzeBtn.disabled = true;
      analyzeBtn.innerHTML = '<span>⚡ Processing AI Multi-Image & XAI Diagnosis...</span>';

      const formData = new FormData();
      selectedFiles.forEach(file => formData.append('leaf_images', file));

      fetch('/predict', {
        method: 'POST',
        body: formData
      })
      .then(res => res.json())
      .then(data => {
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = '<span>🌿 Run AI Multi-Image Diagnostics</span>';
        if (data.error) {
          alert('Analysis Error: ' + data.error);
          return;
        }
        renderDiagnosticResults(data);
      })
      .catch(err => {
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = '<span>🌿 Run AI Multi-Image Diagnostics</span>';
        alert('Network Error: ' + err.message);
      });
    });
  }

  function renderDiagnosticResults(data) {
    if (!resultPlaceholder || !resultContent) return;
    resultPlaceholder.style.display = 'none';
    resultContent.style.display = 'flex';

    // Status & Multi-count
    const badge = document.getElementById('resStatusBadge');
    badge.className = 'badge-status ' + (data.status === 'Healthy' ? 'healthy' : 'diseased');
    badge.innerText = (data.status === 'Healthy' ? '✔ HEALTHY LEAF' : '⚠ DISEASE DETECTED');

    document.getElementById('resMultiCount').innerText = `Multi-Image Consensus (${data.multi_image_count} Image${data.multi_image_count > 1 ? 's' : ''})`;
    document.getElementById('resCropDisease').innerText = `${data.crop} - ${data.disease}`;
    document.getElementById('resScientificName').innerText = data.scientific_name || '';

    // Severity, Urgency, Recovery
    document.getElementById('resSeverityVal').innerText = `${data.severity_level} (${data.severity_percent}%)`;
    document.getElementById('resUrgencyVal').innerText = data.urgency;
    document.getElementById('resRecoveryVal').innerText = data.recovery_time;

    // Confidence meter
    document.getElementById('resConfidenceVal').innerText = `${data.confidence}%`;
    document.getElementById('resConfidenceBar').style.width = `${data.confidence}%`;

    // XAI Explanations
    const xaiList = document.getElementById('resXaiExplanations');
    xaiList.innerHTML = '';
    (data.feature_explanations || []).forEach(exp => {
      const li = document.createElement('li');
      li.innerText = exp;
      xaiList.appendChild(li);
    });

    // Symptoms & Cause
    const symList = document.getElementById('resSymptomsList');
    symList.innerHTML = '';
    (data.symptoms || []).forEach(s => {
      const li = document.createElement('li');
      li.innerText = s;
      symList.appendChild(li);
    });
    document.getElementById('resCauseText').innerText = data.cause || '';

    // Ranked Treatments
    const rankedBox = document.getElementById('resRankedTreatments');
    rankedBox.innerHTML = '';
    (data.ranked_treatments || []).forEach(t => {
      const div = document.createElement('div');
      div.style.background = 'rgba(255,255,255,0.03)';
      div.style.border = '1px solid var(--border-glass)';
      div.style.padding = '8px 12px';
      div.style.borderRadius = '6px';
      div.style.display = 'flex';
      div.style.justifyContent = 'space-between';
      div.style.alignItems = 'center';
      div.innerHTML = `<span><strong style="color: var(--accent-mint);">${t.score}</strong> ${t.name} (${t.type})</span> <a href="/marketplace?search=${encodeURIComponent(t.name.split(' ')[0])}" class="btn-nav" style="padding: 2px 8px; font-size: 0.75rem;">Buy</a>`;
      rankedBox.appendChild(div);
    });

    // Export link
    const exportBtn = document.getElementById('exportReportBtn');
    if (exportBtn && data.scan_id) {
      exportBtn.href = `/export-report/${data.scan_id}`;
    }

    recalculateDosage();
  }

  window.selectSample = function(filename) {
    fetch(`/static/samples/${filename}`)
      .then(res => res.blob())
      .then(blob => {
        const file = new File([blob], filename, { type: 'image/jpeg' });
        handleMultiFiles([file]);
        setTimeout(() => {
          if (analyzeBtn) analyzeBtn.click();
        }, 300);
      });
  };

  window.resetDropzone = function() {
    selectedFiles = [];
    if (leafInput) leafInput.value = '';
    if (previewGrid) previewGrid.innerHTML = '';
    if (previewContainer) previewContainer.style.display = 'none';
    if (dropzone) dropzone.style.display = 'block';
    if (analyzeBtn) analyzeBtn.disabled = true;
    if (resultPlaceholder) resultPlaceholder.style.display = 'block';
    if (resultContent) resultContent.style.display = 'none';
  };
});

// --- DOSAGE CALCULATOR ---
window.recalculateDosage = function() {
  const acresInput = document.getElementById('calcAcresInput');
  const output = document.getElementById('calcDosageOutput');
  if (!acresInput || !output) return;
  const acres = parseFloat(acresInput.value) || 1.0;
  const fungicideMl = Math.round(acres * 240);
  const waterL = Math.round(acres * 80);
  output.innerText = `Required Fungicide Dosage: ${fungicideMl} ml/g • Water Volume Required: ${waterL} Liters`;
};

// --- SHOPPING CART SYSTEM ---
window.addToCart = function(id, name, price) {
  const existing = cart.find(item => item.product_id === id);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ product_id: id, product_name: name, unit_price: price, quantity: 1 });
  }
  localStorage.setItem('ps_cart', JSON.stringify(cart));
  updateCartBadge();
  alert(`Added "${name}" to your shopping cart!`);
};

function updateCartBadge() {
  const badge = document.getElementById('cartBadgeCount');
  if (!badge) return;
  const count = cart.reduce((sum, i) => sum + i.quantity, 0);
  badge.innerText = count;
}

function renderCartPage() {
  const container = document.getElementById('cartItemsContainer');
  const totalVal = document.getElementById('cartTotalVal');
  const cartInput = document.getElementById('cartDataInput');
  if (!container) return;

  if (cart.length === 0) {
    container.innerHTML = '<p style="color: var(--text-muted); text-align:center; padding: 2rem;">Your shopping cart is empty. Browse the Agro-Marketplace to add products.</p>';
    if (totalVal) totalVal.innerText = '$0.00';
    if (cartInput) cartInput.value = '[]';
    return;
  }

  container.innerHTML = '';
  let total = 0;
  cart.forEach((item, index) => {
    const subtotal = item.unit_price * item.quantity;
    total += subtotal;
    const div = document.createElement('div');
    div.style.display = 'flex';
    div.style.justifyContent = 'space-between';
    div.style.alignItems = 'center';
    div.style.padding = '10px 0';
    div.style.borderBottom = '1px solid var(--border-glass)';
    div.innerHTML = `
      <div>
        <strong>${item.product_name}</strong>
        <div style="font-size: 0.8rem; color: var(--text-muted);">$${item.unit_price.toFixed(2)} x ${item.quantity}</div>
      </div>
      <div>
        <strong style="color: var(--accent-mint); margin-right: 12px;">$${subtotal.toFixed(2)}</strong>
        <button type="button" onclick="removeFromCart(${index})" style="background:none; border:none; color:#ef4444; cursor:pointer;">✕</button>
      </div>
    `;
    container.appendChild(div);
  });

  if (totalVal) totalVal.innerText = `$${total.toFixed(2)}`;
  if (cartInput) cartInput.value = JSON.stringify(cart);
}

window.removeFromCart = function(index) {
  cart.splice(index, 1);
  localStorage.setItem('ps_cart', JSON.stringify(cart));
  updateCartBadge();
  renderCartPage();
};

// --- AGRIBOT AI VOICE & CHATBOT ---
window.sendChatMessage = function() {
  const input = document.getElementById('chatInput');
  const chatBox = document.getElementById('chatBox');
  if (!input || !chatBox || !input.value.trim()) return;

  const userQuery = input.value.trim();
  input.value = '';

  const userDiv = document.createElement('div');
  userDiv.style.background = 'rgba(255,255,255,0.08)';
  userDiv.style.padding = '8px 12px';
  userDiv.style.borderRadius = '10px';
  userDiv.style.alignSelf = 'flex-end';
  userDiv.style.maxWidth = '80%';
  userDiv.innerHTML = `<strong>👤 You:</strong> ${userQuery}`;
  chatBox.appendChild(userDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  const currentLang = localStorage.getItem('ps_language') || 'en';

  fetch('/api/chatbot', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: userQuery, lang: currentLang })
  })
  .then(res => res.json())
  .then(data => {
    const aiDiv = document.createElement('div');
    aiDiv.style.background = 'rgba(16,185,129,0.15)';
    aiDiv.style.border = '1px solid var(--border-active)';
    aiDiv.style.padding = '8px 12px';
    aiDiv.style.borderRadius = '10px';
    aiDiv.style.alignSelf = 'flex-start';
    aiDiv.style.maxWidth = '85%';
    aiDiv.innerHTML = `<strong>🤖 AgriBot AI:</strong><br>${data.reply}`;
    chatBox.appendChild(aiDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Speech synthesis audio reply
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(data.reply);
      utterance.lang = currentLang === 'ta' ? 'ta-IN' : (currentLang === 'hi' ? 'hi-IN' : 'en-US');
      window.speechSynthesis.speak(utterance);
    }
  });
};

window.sendQuickPrompt = function(promptText) {
  const input = document.getElementById('chatInput');
  if (input) {
    input.value = promptText;
    sendChatMessage();
  }
};

window.toggleVoiceInput = function() {
  if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    alert('Voice recognition is not supported in this browser. Please use Chrome or Edge.');
    return;
  }
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  const currentLang = localStorage.getItem('ps_language') || 'en';
  recognition.lang = currentLang === 'ta' ? 'ta-IN' : (currentLang === 'hi' ? 'hi-IN' : 'en-US');

  const btn = document.getElementById('voiceMicBtn');
  if (btn) btn.style.color = '#ef4444';

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    const input = document.getElementById('chatInput');
    if (input) {
      input.value = transcript;
      sendChatMessage();
    }
    if (btn) btn.style.color = '#fff';
  };

  recognition.onerror = () => {
    if (btn) btn.style.color = '#fff';
  };

  recognition.start();
};
