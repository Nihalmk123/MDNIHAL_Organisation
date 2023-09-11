
        function hideToast(button) {
            const toast = button.parentNode;
            toast.classList.remove('show');
            setTimeout(() => {
              toast.remove();
            }, 300); // Remove the toast after 0.5 seconds (adjust the value as needed)
          }

          // Automatically hide the toasts after 5 seconds (or adjust the value as needed)
          document.addEventListener('DOMContentLoaded', function() {
            const toasts = document.querySelectorAll('.toast');
            toasts.forEach((toast, index) => {
              setTimeout(() => {
                hideToast(toast.querySelector('.close-button'));
              }, (index + 1) * 3000); // Show each toast for 5 seconds
            });
          });