

$(document).ready(function () {

  // Voir plus / Voir moins
  const $toggleBtn = $('#toggle-btn');
  const $listWrapper = $('.list-wrapper');
  if ($toggleBtn.length && $listWrapper.length) {
    $toggleBtn.on('click', function () {
      $listWrapper.toggleClass('expanded');
      $toggleBtn.text($listWrapper.hasClass('expanded') ? 'Voir moins' : 'Voir plus');
    });
  }

  // Sélectionner / désélectionner tous les checkboxes
  const $selectAll = $('#select-all');
  const $checkboxes = $('.row-checkbox');

  if ($selectAll.length && $checkboxes.length) {
    $selectAll.on('change', function () {
      const checked = $(this).is(':checked');
      $checkboxes.prop('checked', checked);
    });
  }

  // Soumission du formulaire
  const $form = $('#qr-form');
  const $hiddenInput = $('#selected-ids');

  if ($form.length && $hiddenInput.length) {
    $form.on('submit', function (e) {
      e.preventDefault();
      const selectedIds = $('.row-checkbox:checked').map(function () {
        return $(this).val();
      }).get();

      if (selectedIds.length === 0) {
        alert("Veuillez sélectionner au moins un adhérent.");
        return;
      }

      $hiddenInput.val(selectedIds.join(','));

      // Décommente si tu veux vraiment envoyer
       this.submit();

      // Pour test
      console.log("Soumission avec IDs :", selectedIds);
    });
  }

  // Filtrage des cours par dojo (ajouter/modifier adhérent)
  function filterCoursesByDojo() {
    const $dojoSelect = $('.ajouter-add-dojo, .modifier-add-dojo');
    if ($dojoSelect.length && $('.form-check-all').length) {
      // Fonction de filtrage
      function applyFilter() {
        const selectedDojoId = $dojoSelect.val();
        
        // Cacher tous les cours
        $('.form-check-all .form-check').hide();
        
        if (selectedDojoId) {
          // Afficher uniquement les cours du dojo sélectionné
          $('.form-check-all .form-check.dojo-' + selectedDojoId).show();
        }
      }
      
      // Écouter les changements
      $dojoSelect.on('change', applyFilter);
      
      // Appliquer le filtrage au chargement
      applyFilter();
    }
  }

  // Filtrage des profs par dojo (modifier cours)
  function filterProfsByDojo() {
    const $dojoSelectModifier = $('.modifier-add-dojo');
    if ($dojoSelectModifier.length && $('.form-check-all').length) {
      // Cette fonctionnalité peut être ajoutée si nécessaire
      // Pour l'instant, on garde tous les profs visibles
    }
  }

  // Initialiser les filtres
  filterCoursesByDojo();
  filterProfsByDojo();

});

