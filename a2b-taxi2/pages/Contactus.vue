<template>
  <div class="container contact-us mt-4">
    <div class="row">
      <div class="col-md-7">
        <h4 class="theme-clr">
          Contact Us
        </h4>
        <h5>We are available 24/7, Feel free to ask any questions.</h5>
        <div v-if="sent" class="alert alert-success mt-2" role="alert">
          <b>Your Message has been sent successfuly , we will contact you shortly</b>
        </div>
        <div v-if="failed" class="alert alert-danger mt-2" role="alert">
          <b>Failed to send your message, please try again</b>
        </div>
        <div class="content">
          <form name="contact" action="" method="post" @submit.prevent="sendEmail">
            <h5>Name</h5>
            <input
              id="name"
              v-model="name"
              type="text"
              placeholder="Enter your name"
              class="form-field d-block w-100 px-1 pt-1"
              name="name"
              required
            >
            <h5 class="mb-0">
              Phone No
            </h5>
            <input v-model="phone" class="w-50 px-1 pt-1 phone" placeholder="Enter your phone" type="tel" required>
            <h5 class="d-xl-inline-block ml-0 ml-xl-3 mt-3 mt-xl-0 mt-0">
              Email
            </h5>
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="Enter your email"
              class="form-field px-1 pt-1 float-right"
              required
            >
            <h5>Message</h5>
            <textarea
              id="message"
              v-model="msg"
              rows="10"
              class="form-field d-block w-100 rounded px-1 pt-1"
              placeholder="Leave your message"
              name="message"
              required
            />
            <input class="form-button thme-btn hover-effect rounded float-right mt-3" type="submit" :value="btnText">
          </form>
        </div>
      </div>
      <div class="col-md-5">
        <h4 class="theme-clr">
          Get in touch with us!
          <div class="unit mt-4">
            <h5>Head Office Address</h5>
            <p>179 Henshaw St, OL1 2BP Oldham, United Kingdom</p>
          </div>
          <div class="unit">
            <h5>Phone Number</h5>
            <a class="text-white" href="tel:0161 213 1111"><p>0161 213 1111</p></a>
          </div>
          <div class="unit">
            <h5>Email Address</h5>
            <a class="text-white" href="mailto:a2btommyfieldcars@gmail.com"><p>a2btommyfieldcars@gmail.com</p></a>
          </div>
          <div class="unit-map">
            <GmapMap
              :center="{lat:53.54760000, lng:-2.11403000}"
              :zoom="16"
              map-type-id="terrain"
              class="map"
            >
              <GmapMarker
                :position="{lat:53.54760000, lng:-2.11403000}"
                :clickable="true"
                :draggable="true"

              />
            </GmapMap>
          </div>
        </h4>
      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
import Vue from 'vue'
export default {
  data() {
    return {
      email: '',
      phone: '',
      msg: '',
      name: '',
      btnText: ' Send Message',
      sent: '',
      failed: ''
    }
  },
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
  },

  methods: {
    sendEmail() {
      const self = this
      self.failed = false
      self.sent = false
      if (!self.status) {
        self.btnText = 'Submitting...'

        const data = {
          // TODO: Use mapState
          name: self.name,
          phone_num: self.phone,
          email: self.email,
          message: self.msg
        }

        Vue.axios.post('/contact/', data)
          .then(function (response) {
            self.sent = true
            self.btnText = 'Send Message'
            self.email = ''
            self.phone = ''
            self.msg = ''
            self.name = ''
          })
          .catch(() => {
            self.failed = true
            self.email = ''
            self.phone = ''
            self.msg = ''
            self.name = ''
          })
      }
    }
  }
}
</script>
