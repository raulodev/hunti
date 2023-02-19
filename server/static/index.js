$(document).ready(function () {
  // formatear el nombre del dominio en la vista previa de la web
  function domain_from_url(url) {
    var result;
    var match;
    if ((match = url.match(/^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n\?\=]+)/im))) {
      result = match[1];
      if ((match = result.match(/^[^\.]+\.(.+\..+)$/))) {
        result = match[1];
      }
    }
    return result;
  }

  $("*")
    .find("#domain")
    .each(function () {
      $(this).html(function (_, html) {
        let domain = domain_from_url(html);
        return (html = domain);
      });
    });

  // Cambiar los saltos de linea
  $("*")
    .find("#text")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/\n/g, "<br/>");
      });
    });

  // Cambiar el color en las palabras que contengan el símbolo (#) por delante
  $("*")
    .find("#text")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\#\w+)/g, '<span style="color:#1D9BF0">$1</span>');
      });
    });

  // Cambiar el color en las palabras que contengan el símbolo (@) por delante
  $("*")
    .find("#text")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\@\w+)/g, '<span style="color:#1D9BF0">$1</span>');
      });
    });

  // eliminar los enlaces de twitter
  $("*")
    .find("#text")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\https:\/\/t.co\/\w+)/g, "");
      });
    });

  // Cambiar el color a los enlaces en el texto
  $("*")
    .find("#text")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(?:https?|ftp):\/\/[\n\S]+/g, '<span style="color:#1D9BF0">$&</span>');
      });
    });

  // Cambiar el formato de la hora dada por el api de twitter a hora local de Cuba
  $("*")
    .find("#date")
    .each(function () {
      let date = new Date($(this).text());

      options = {
        day: "numeric",
        month: "short",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        timeZone: "America/Havana",
      };

      $(this).text(`${new Intl.DateTimeFormat("es-Es", options).format(date)}`);
    });

  // Mostrar porciento de las encuestas
  $("*")
    .find("#poll")
    .each(function () {
      // Obtener una lista con los votos de la encuesta
      let lista_de_votos = [];

      $(this)
        .find(".vote-count")
        .each(function () {
          const votos = Number($(this).text());
          lista_de_votos.push(votos);
        });

      // Obtener el total de votos
      let total = 0;
      for (let v of lista_de_votos) total += v;

      // función para calcular el porciento
      function porciento(part, total) {
        p = (part / total) * 100;
        num = p.toFixed(1);
        if (num.toString().includes(".0")) {
          return p.toFixed();
        } else {
          return p.toFixed(1);
        }
      }

      // Cambiamos el ancho del fondo en las encuestas segun los votos
      $(this)
        .find(".vote-bg")
        .each(function (index, e) {
          por = porciento(lista_de_votos[index], total);
          if (por == 0) {
            e.style.width = "1%";
          } else {
            e.style.width = por + "%";
          }
        });

      // Cambiamos el # mostrado en el porciento
      $(this)
        .find(".vote-count")
        .each(function (index, e) {
          e.textContent = porciento(lista_de_votos[index], total);
        });
    });
});

// Para los tweets citados

$(document).ready(function () {
  // formatear el nombre del dominio en la vista previa de la web
  function domain_from_url(url) {
    var result;
    var match;
    if ((match = url.match(/^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n\?\=]+)/im))) {
      result = match[1];
      if ((match = result.match(/^[^\.]+\.(.+\..+)$/))) {
        result = match[1];
      }
    }
    return result;
  }

  $("*")
    .find("#domain_")
    .each(function () {
      $(this).html(function (_, html) {
        let domain = domain_from_url(html);
        return (html = domain);
      });
    });

  // Cambiar los saltos de linea
  $("*")
    .find("#text_")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/\n/g, "<br/>");
      });
    });

  //  Cambiar el color en las palabras que contengan el símbolo (#) por delante
  $("*")
    .find("#text_")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\#\w+)/g, '<span style="color:#1D9BF0">$1</span>');
      });
    });
  //  Cambiar el color en las palabras que contengan el símbolo (@) por delante
  $("*")
    .find("#text_")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\@\w+)/g, '<span style="color:#1D9BF0">$1</span>');
      });
    });
  // eliminar los enlaces de twitter
  $("*")
    .find("#text_")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(\https:\/\/t.co\/\w+)/g, "");
      });
    });
  // Cambiar el color a los enlaces en el texto
  $("*")
    .find("#text_")
    .each(function () {
      $(this).html(function (_, html) {
        return html.replace(/(?:https?|ftp):\/\/[\n\S]+/g, '<span style="color:#1D9BF0">$&</span>');
      });
    });
  // Cambiar el formato de la hora dada por el api de twitter a hora local de Cuba
  $("*")
    .find("#date_")
    .each(function () {
      let date = new Date($(this).text());

      options = {
        day: "numeric",
        month: "short",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        timeZone: "America/Havana",
      };

      $(this).text(`${new Intl.DateTimeFormat("es-Es", options).format(date)}`);
    });
  // Mostrar porciento de las encuestas
  $("*")
    .find("#poll_")
    .each(function () {
      // Obtener una lista con los votos de la encuesta
      let lista_de_votos = [];

      $(this)
        .find(".vote-count_")
        .each(function () {
          const votos = Number($(this).text());
          lista_de_votos.push(votos);
        });

      // Obtener el total de votos
      let total = 0;
      for (let v of lista_de_votos) total += v;

      // función para calcular el porciento
      function porciento(part, total) {
        p = (part / total) * 100;
        num = p.toFixed(1);
        if (num.toString().includes(".0")) {
          return p.toFixed();
        } else {
          return p.toFixed(1);
        }
      }

      // Cambiamos el ancho del fondo en las encuestas segun los votos
      $(this)
        .find(".vote-bg_")
        .each(function (index, e) {
          por = porciento(lista_de_votos[index], total);
          if (por == 0) {
            e.style.width = "1%";
          } else {
            e.style.width = por + "%";
          }
        });

      // Cambiamos el # mostrado en el porciento
      $(this)
        .find(".vote-count_")
        .each(function (index, e) {
          e.textContent = porciento(lista_de_votos[index], total);
        });
    });
});
