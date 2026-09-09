// Meta Pixel & Conversions API Tracking Helper
(function() {
  window.PulseAnalytics = {
    pixelId: '102938475610293',
    
    generateEventId: function(prefix) {
      return (prefix || 'evt') + '_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
    },

    init: function() {
      if (!window.fbq) {
        var n = window.fbq = function() {
          n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
        };
        if (!window._fbq) window._fbq = n;
        n.push = n; n.loaded = !0; n.version = '2.0';
        n.queue = [];
        var t = document.createElement('script');
        t.async = !0; t.src = 'https://connect.facebook.net/en_US/fbevents.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
      }
      
      try {
        window.fbq('init', this.pixelId);
        window.fbq('track', 'PageView');
        console.log('[Meta Pixel] Initialized PageView');
      } catch(e) {
        console.log('[Meta Pixel Initialized (Simulated)]', e);
      }
    },

    trackEvent: function(eventName, params, eventId) {
      var evtId = eventId || this.generateEventId(eventName.toLowerCase());
      try {
        if (window.fbq) {
          window.fbq('track', eventName, params, { eventID: evtId });
        }
      } catch (e) {}
      console.log('[Meta Pixel Tracked]', eventName, params, 'eventID:', evtId);
      return evtId;
    }
  };

  window.PulseAnalytics.init();
})();
