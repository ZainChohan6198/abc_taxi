<template>
  <header id="main-header" class="w-100">
    <div class="container px-0 ">
      <div class="row w-100">
        <div class="col-md-12">
          <nav class="navbar navbar-expand-lg navbar-light py-0">
            <div id="navbarNavDropdown" :class="[{hide: this.$store.state.hide}]"  class="collapse navbar-collapse justify-content-center">
              <ul class="navbar-nav">
                <li class="nav-item active">
                  <nuxt-link class="nav-link mx-0 mr-xl-4" to="/">
                    Home
                  </nuxt-link>
                </li>
                <li class="nav-item active">
                  <nuxt-link class="nav-link mx-0 mx-xl-3"  to="/abouts">
                    About Us
                  </nuxt-link>
                </li>
                <li class="nav-item active">
                  <nuxt-link class="nav-link mx-0 mx-xl-3"  to="/form">
                    Book Online
                  </nuxt-link>
                </li>
                <li class="nav-item active">
                  <nuxt-link class="nav-link mx-0 mx-xl-3"  to="/support">
                    Support
                  </nuxt-link>
                </li>
                <li class="nav-item active">
                  <nuxt-link class="nav-link mx-0 mx-xl-3" to="/airport-transfers">
                    Airport Transfer
                  </nuxt-link>
                </li>

                <li class="nav-item active" >
                  <nuxt-link class="nav-link mx-0 mx-xl-3" to="/Contactus">
                    Contact Us
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </header>
</template>
