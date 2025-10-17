document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('architecture-btn');
  const output = document.getElementById('architecture-text');
  const modal = document.getElementById('architecture-modal');
  const closeModalBtn = document.getElementById('close-architecture-modal');

  const openModal = () => {
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    modal.focus();
  };

  const closeModal = () => {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    button.focus();
  };

  button.addEventListener('click', () => {
    openModal();
  });

  closeModalBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });
});
