/* vergleichsdoch – kleine Interaktionen
   Färbt die Detailtabelle als Heatmap ein (dunkler = besserer Score). */
(function () {
  "use strict";

  function heatColor(score) {
    // score 0..10 -> Farbverlauf von hellgrau (schwach) zu teal (stark)
    var t = Math.max(0, Math.min(1, score / 10));
    // Basisfarbe Teal (#0f9d8c) mit steigender Deckkraft
    var alpha = 0.08 + t * 0.55;
    return "rgba(15, 157, 140, " + alpha.toFixed(3) + ")";
  }

  function textColor(score) {
    return score >= 8 ? "#0a3f38" : "#1a2b3d";
  }

  function paintHeatmap() {
    var cells = document.querySelectorAll("#heatTable tbody td.heat");
    cells.forEach(function (cell) {
      var val = parseFloat(cell.textContent.trim().replace(",", "."));
      if (isNaN(val)) return;
      cell.style.background = heatColor(val);
      cell.style.color = textColor(val);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", paintHeatmap);
  } else {
    paintHeatmap();
  }
})();
