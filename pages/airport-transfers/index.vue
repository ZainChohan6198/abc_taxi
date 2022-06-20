<template>
  <div id="airport-transfer" class="titlepage-wrapper">
    <div class="container title-aboutus">
      <div class="row mt-3">
        <div class="col-12">
          <img alt="airpot transfer" src="~assets/img/airporttransfer.png"><h4 class="theme-clr">
            Airport Transfer
          </h4>
          <p>
            To ease airport passengers, we offer airport transport service that is safe, reliable and comes
            within everyone’s budget. Whether you need a taxi in urgent or want to pre-book to beat rush hours,
            we are available 24 hours a day with executive airport taxis for you. Now, you can get to any airport in
            the UK in time without worrying about your flight.With Sat Nav equipped vehicles, there is a reason we are
            amongst the top-rated taxis companies in the UK.
            We provide ideal taxi rides that are soothing and perfect for airport pick & drop. Just book, relax and let
            us take you to the destination by offering peaceful cosy drives. With GPS devices installed, our chauffeurs
            will take you through non-congested routes.
          </p>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-12">
          <img alt="nearest airport" src="~assets/img/nearestairport.png"><h4 class="theme-clr">
            Nearest Airports to Oldham
          </h4>
          <div class="unit">
            <span>Oldham to Manchester Airport (MAN)  </span><p>
              It is the closest airport to Oldham situated 18.7
              miles (30 mins). Manchester Airport facilitates over 28 million passengers per year. Travel to Manchester
              Airport from Oldham with us at prices you wouldn’t believe.
            </p>
          </div>
          <div class="unit">
            <span>Oldham to Leeds Bradford Airport (LBA)  </span><p>
              Residing 39 miles away from Oldham, Leeds Bradford
              Airport is amongst few UK airports to have busiest routes to and from Europe. Want to know why? Let’s travel
              to Leeds Bradford Airport and see for ourselves.
            </p>
          </div>
          <div class="unit">
            <span>Oldham to Liverpool John Lennon Airport (LPL)  </span><p>
              Named after the famous singer John Lennon from
              the Beatles, Liverpool Airport (43.2 miles away) offers magnificent travel packages to Europe. Find out more
              by travelling in a taxi to Liverpool Airport with us.
            </p>
          </div>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-12">
          <img alt="price" src="~assets/img/price.png"><h4 class="theme-clr">
            Example Rates
          </h4>
          <table class="table table-striped mt-2">
            <thead>
              <tr>
                <th scope="col">
                  From
                </th>
                <th scope="col">
                  To
                </th>
                <th scope="col">
                  Price starts from
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Oldham</td>
                <td>MANCHESTER AIRPORT</td>
                <td>&#163; 20</td>
              </tr>
              <tr>
                <td>Oldham</td>
                <td>Leeds Bradford Airport</td>
                <td>&#163; 45</td>
              </tr>
              <tr>
                <td>Oldham</td>
                <td>LIVERPOOL AIRPORT</td>
                <td>&#163; 50</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  mounted() {
    const self = this
    self.$store.dispatch('resetState')
    self.$store.commit('hide', true)
    this.timeout = setTimeout(function () {
      self.$store.commit('hide', false)
    }, 500)
  },
  destroyed() {
    clearTimeout(this.timeout)
    this.$store.commit('hide', false)
  }
}
</script>
