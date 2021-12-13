<template>
  <div class="wrapper-info">
    <div class="container">
      <div class="row">
        <div class="col-2 logo">
          <img alt="logo" src="~assets/img/logo.png" @click="goHome">
        </div>
        <div class=" col-2 phone d-none d-xl-block py-5">
          <i class="fa fa-phone-square" aria-hidden="true" />
          <a class="text-white" href="tel:0161 213 1111"><span>0161 213 1111</span></a>
        </div>
        <div class="col-md-4 address py-5 d-none d-xl-block">
          <a class="text-white" href="mailto:a2btommyfieldcars@gmail.com"><i class="fa fa-envelope mr-1" /><span>a2btommyfieldcars@gmail.com</span></a>
          <span />
        </div>
        <div class="col-md-4 address py-5 d-none d-xl-block">
          <i class="fa fa-address-book" aria-hidden="true" />
          <span>179 Henshaw St,
            OL1 2BP Oldham, United Kingdom</span>
        </div>
        <div class=" col-9 d-lg-none py-5 become-driver ">
          <button
            class="navbar-toggler float-right mr-2"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
export default {
  methods: {
    goHome() {
      if (this.$route.path === '/') {
        window.location = '/'
      } else {
        this.$router.push({ path: '/' })
      }
    }
  }
}
</script>
