main();

/**
 * Configura a aplicação frontend
 */
function main() {
    const form = document.getElementById("heart-disease-form");
    form.addEventListener("submit", handleSubmit);
}

/**
 * Orquestra a busca e renderização da predição quando o evento de submit é disparado
 *
 * @param {SubmitEvent} event
 */
async function handleSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const prediction = await makePrediction(form);
    renderHeartDiseaseMessage(prediction, form);
}

/**
 * Faz a predição de doença cardíaca (backend)
 *
 * @param {HTMLFormElement} form
 * @returns {Promise<string>}
 */
async function makePrediction(form) {
    const formData = new FormData(form);
    const url = "http://localhost:8080";
    const response = await fetch(url, { method: "POST", body: formData });
    const data = await response.json();
    return data.prediction;
}

/**
 * Renderiza as informações de predição
 *
 * @param {string} message display message
 * @param {HTMLFormElement} form form element
 */
function renderHeartDiseaseMessage(message, form) {
    form.remove();
    const container = document.getElementById("container");
    const resultContainer = createResultContainer(message);
    const retryBtn = createRetryButton();
    resultContainer.insertAdjacentElement("beforeend", retryBtn);
    container.insertAdjacentElement("beforeend", resultContainer);
}

/**
 * Cria o elemento container de resultado
 *
 * @param {string} message
 * @returns {HTMLDivElement}
 */
function createResultContainer(message) {
    const resultContainer = document.createElement("div");
    resultContainer.classList.add("result-container");
    resultContainer.textContent = `Resultado: ${message}`;
    return resultContainer;
}

/**
 * Cria o elemento botão de retentativa
 *
 * @returns {HTMLDivElement}
 */
function createRetryButton() {
    const retryBtn = document.createElement("button");
    retryBtn.textContent = "Fazer outro teste";
    retryBtn.onclick = () => location.reload();
    return retryBtn;
}
