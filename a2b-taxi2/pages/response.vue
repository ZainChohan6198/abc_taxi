<template>
  <div class="booking">
    <div class="overlay">
      <div id="main-hero" class="home-hero">
        <div class="container">
          <div v-if="$store.state.booking_status && $route.path == '/response'" class="row justify-content-center">
            <div class="col-12 col-md-10 px-1 px-md-3">
              <p class="notify">
                You will recieve a text once the driver has been assigned to your booking
              </p>
              <section class="booking-info">
                <header>
                  <h3 class="text-center">
                    {{ $store.state.icabbi_status }}...
                  </h3>
                  <div v-if="$store.state.driver_id" class="row justify-content-center driver-info mt-3 mb-2">
                    <div class="col-md-6 driver rounded">
                      <table class="table h-100">
                        <tbody>
                          <tr>
                            <th scope="row">
                              <i class="fa fa-user-circle-o" aria-hidden="true" />
                            </th>
                            <td>{{ $store.state.driver_name.replace(/ .*/,'') }}</td>
                          </tr>
<!--                          <tr>-->
<!--                            <th scope="row">-->
<!--                              <i class="fa fa-volume-control-phone" aria-hidden="true" />-->
<!--                            </th>-->
<!--                            <td><a>{{ $store.state.driver_mobile }}</a></td>-->
<!--                          </tr>-->
                          <tr>
                            <th scope="row">
                              <i class="fa fa-car" aria-hidden="true" />
                            </th>
                            <td>
                              {{ $store.state.no_plate }}
                              <div class="mt-1">
                                <i>{{ $store.state.driver_make }}</i><i class="ml-1">{{ $store.state.driver_model }}</i>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div class="col-md-6">
                      <gmap-map
                        :center="center"
                        :zoom="14.6">
                        <GmapCustomMarker
                          :marker="markers">
                          <img src="~assets/img/driver.png"/>
                        </GmapCustomMarker>
                      </gmap-map>
                    </div>
                  </div>
                  <span>Booking ID</span><span class="text-success"> #{{ $store.state.id }}</span>
                </header>

                <div class="unit pickup mt-2">
                  <i class="fa fa-map-marker" aria-hidden="true" />
                  <b>Pickup</b>
                  <p>{{ $store.state.pickup_address }}</p>
                </div>
                <div class="unit pickup">
                  <i class="fa fa-map-marker" aria-hidden="true" />
                  <b>Drop Off</b>
                  <p>{{ $store.state.dropoff_address }}</p>
                </div>
                <div v-if="$store.state.via1_id || $store.state.via2_id || $store.state.via3_id" class="unit pickup">
                  <b>Vias</b>
                  <p class="mb-1">
                    {{ $store.state.via1_address }}
                  </p>
                  <p class="mb-1">
                    {{ $store.state.via2_address }}
                  </p>
                  <p class="mb-1">
                    {{ $store.state.via3_address }}
                  </p>
                </div>
                <div class="unit pickup d-flex">
                  <div class="w-50">
                    <i class="fa fa-calendar" aria-hidden="true" />
                    <b>Pickup Date</b>
                    <p v-if="$store.state.pickup_date">
                      {{ $store.state.pickup_date | moment('MMM DD ,gggg, h:mma') }}
                    </p>
                    <p v-else>
                      ASAP
                    </p>
                  </div>
                  <div v-if="$store.state.return_date" class="w-50">
                    <i class="fa fa-calendar" aria-hidden="true" />
                    <b>Return Date</b>
                    <p v-if="$store.state.return_date">
                      {{ $store.state.return_date | moment('MMM DD ,gggg, h:mma') }}
                    </p>
                    <p v-else>
                      ASAP
                    </p>
                  </div>
                </div>
                <div class="unit pickup d-flex">
                  <div class="w-50">
                    <i class="fa fa-user" aria-hidden="true" />
                    <b>Passenger Info</b>
                    <p>{{ $store.state.name }}</p>
                    <p>{{ $store.state.phone }}</p>
                    <p>{{ $store.state.email }}</p>
                  </div>
                  <div class="w-50">
                    <b>Vehicle</b>
                    <p>{{ $store.state.vehicle_title }}</p>
                  </div>
                </div>
                <div v-if="$store.state.icabbi_status" class="unit pickup">
                  <b>Status</b>
                  <p>{{ $store.state.icabbi_status }}</p>
                </div>
                <div class="unit pickup">
                  <i class="fa fa-money" aria-hidden="true" />
                  <b>Est. Fare</b>
                  <p class="display-4">
                    &#163;{{ $store.state.price }}
                  </p>
                </div>
                <div class="buttons text-center">
                  <button class="standard-btn hover-effect px-2 py-2" @click="makeOther">
                    <i class="fa fa-location-arrow mr-1" aria-hidden="true" />Make Another
                  </button>
                  <button class="standard-btn hover-effect px-2 py-2" @click="home">
                    <i class="fa fa-home mr-1" aria-hidden="true" />Homepage
                  </button>
                </div>
              </section>
            </div>
          </div>
          <!--          <i class="fa fa-check" aria-hidden="true" />-->
          <!--          <h3>Your ride has been booked with ID <b class="text-success">{{$store.state.id}}</b> , details have been sent to your number</h3>-->
        </div>
      </div>
      <div v-if="!$store.state.booking_status && $route.path == '/response'" class="response text-center">
        <div class="response-content ">
          <i class="fa fa-exclamation-triangle " aria-hidden="true" />
          <h3 class="text-light">
            We find no driver near selected location , please try after sometime
          </h3>
          <div class="buttons text-center">
            <button class="standard-btn hover-effect" @click="makeOther">
              <i class="fa fa-location-arrow " aria-hidden="true" />Make Another
            </button>
            <button class="standard-btn hover-effect" @click="home">
              <i class="fa fa-home" aria-hidden="true" />Homepage
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
import Vue from 'vue'
import GmapCustomMarker from 'vue2-gmap-custom-marker'
export default {
  scrollToTop: true,
  components: {
    GmapCustomMarker
  },
  data() {
    return {
      trackStatus: false,
      cancel: '',
      show: true
    }
  },
  computed: {
    markers() {
      return { lat: this.$store.state.driver_lat, lng: this.$store.state.driver_lng }
    },
    center() {
      return { lat: this.$store.state.driver_lat, lng: this.$store.state.driver_lng }
    }
  },
  mounted() {
    const self = this
    if (!self.$store.state.droppoff_id && !self.$store.state.id) {
      self.$router.push({ path: '/' })
    }
    self.timeout = setTimeout(function () {
      self.getBooking()
      self.interval = setInterval(function () {
        self.getBooking()
      }, 10000)
    }, 3000)
  },
  destroyed() {
    clearTimeout(this.timeout)
    clearInterval(this.interval)
    this.$store.dispatch('resetState')
  },
  methods: {
    home() {
      this.$router.push({ path: '/' })
      this.$store.dispatch('resetState')
    },
    makeOther() {
      this.$router.push({ path: '/form' })
      this.$store.dispatch('resetState')
    },
    getBooking(initial = false) {
      const self = this
      self.$store.commit('loader', true)
      if (self.$store.state.id) {
        Vue.axios.get('/booking/' + self.$store.state.id)
          .then(function (response) {
            self.$store.commit('icabbi_status', response.data.icabbi_status)
            self.$store.commit('booking_status', response.data.booking_status)
            self.$store.commit('name', response.data.name)
            self.$store.commit('pickup_address', response.data.pickup.formatted)
            self.$store.commit('dropoff_address', response.data.dropoff.formatted)
            self.$store.commit('vehicle_title', response.data.vehicle_title)
            self.$store.commit('id', response.data.id)
            self.$store.commit('driver', response.data.driver)
            if (self.$store.state.id) {
              self.$store.commit('loader', false)
            }
          })
          .catch((error) => {
            self.$store.commit('loader', false)
            self.trackStatus = true
          })
      }
    },
    deleteBook() {
      const self = this
      self.$store.commit('loader', true)
      Vue.axios.delete('/booking/' + this.$store.state.id)
        .then(function (response) {
          self.$store.commit('loader', false)
          self.cancel = 'cancelled'
          self.show = false
        })
        .catch(() => {
          self.$store.commit('loader', false)
          self.cancel = 'failed'
          self.show = false
        })
    }
  }
}
</script>
