<template>
  <div id="aboutuse" class="titlepage-wrapper">
    <div class="container title-aboutus">
      <div class="row mt-3">
        <div class="col-12">
          <h4 class="theme-clr">
            About Us
          </h4>
          <p>
            Welcome to A2B Tommyfield Cars where our customers benefit from over 100 vehicles that are available to
            transport you 24/7 anywhere in the UK. We have introduced an affordable fare for our customers and ever
        since been rewarded with many loyal customers. We can provide a vehicle to suit any journey. Our large fleet allows us to supply prestige & executive
            vehicles for special occasions to standard cars that will get you from A to B.
            We also have a range of Airport taxis to take you from or to any airport in the UK.
          </p>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-12">
          <h4 class="theme-clr">
            Our Services
          </h4>
          <ul>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              100% Customer-Satisfaction
            </li>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              No Hidden Charges, No Extra Costs
            </li>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              Fixed Prices
            </li>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              Fast & Safe Airport Transfers
            </li>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              Nationwide
            </li>
            <li>
              <i class="fa fa-check" aria-hidden="true" />
              Secure Online & App Booking
            </li>
          </ul>
        </div>
      </div>
      <div class="row mt-2">
        <div class="col-12">
          <div class="testemonial text-center ">
            <div class="main-content">
              <h5>Client</h5>
              <h3 class="theme-clr">
                Testimonial
              </h3>
            </div>
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" data-interval="5000">
              <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active" />
                <li data-target="#carouselExampleIndicators" data-slide-to="1" />
                <li data-target="#carouselExampleIndicators" data-slide-to="2" />
              </ol>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <div class="container">
                    <div class="row">
                      <div class="col-md-12">
                        <div class="content">
                          <div class="review text-left">
                            <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                            <h3 class="remarks">
                              VERY GOOD TAXI SERVICE
                            </h3>
                            <p>
                              Very good taxi service, always on time and the staff are really nice and easy to talk to.
                              will definitely use them again and I recommend that everybody else does too. BEST TAXI SERVICE IN OLDHAM!!!!!!
                            </p>
                            <div class="client-info">
                              <div class="dp-cover">
                                <img alt="dp female" src="~assets/img/client-dp-female.png">
                              </div>
                              <div class="rating">
                                <span>Emma wilson</span><span>-</span>
                                <span>Customer</span>
                                <span>              <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" /></span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="carousel-item ">
                  <div class="container">
                    <div class="row">
                      <div class="col-md-12">
                        <div class="content">
                          <div class="review text-left">
                            <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                            <h3 class="remarks">
                              BRILLIANT SERVICES
                            </h3>
                            <p>
                              I absolutely LOVE A2B Taxis, they never fail to let me down and are always there when I
                              need them! They're FAB! Great prices and a brilliant service!
                            </p>
                            <div class="client-info">
                              <div class="dp-cover">
                                <img alt="dp female" src="~assets/img/client-dp-female.png">
                              </div>
                              <div class="rating">
                                <span>Emily Jayne</span><span>-</span>
                                <span>Customer</span>
                                <span>
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                </span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="carousel-item">
                  <div class="container">
                    <div class="row">
                      <div class="col-md-12">
                        <div class="content">
                          <div class="review text-left">
                            <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                            <h3 class="remarks">
                              ALL PERFECT!
                            </h3>
                            <p>
                              Cheap prices quick driving freshie drivers all perfect
                            </p>
                            <div class="client-info">
                              <div class="dp-cover">
                                <img alt="dp male" src="~assets/img/client-dp-male.png">
                              </div>
                              <div class="rating">
                                <span>Graciano Luvunga</span><span>-</span>
                                <span>Customer</span>
                                <span>              <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" />
                                  <i class="fa fa-star" aria-hidden="true" /></span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
    this.time = setTimeout(function () {
      self.$store.commit('hide', false)
    }, 500)
  },
  destroyed() {
    clearTimeout(this.timeout)
    this.$store.commit('hide', false)
  }
}
</script>
