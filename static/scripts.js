document.addEventListener('DOMContentLoaded', function() {
    const feedbacks = document.querySelectorAll('.feedback');

    feedbacks.forEach(feedback => {
        feedback.addEventListener('click', function() {
            const promptText = this.innerText;
            const essayContainer = document.getElementById('highlighted-essay');
            const currentEssay = essayContainer.innerHTML;
            const updatedEssay = currentEssay.replace(promptText, `<span class="applied-prompt">${promptText}</span>`);
            essayContainer.innerHTML = updatedEssay;
        });
    });
});
